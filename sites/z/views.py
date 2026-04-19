from __future__ import annotations

from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from sites.z.models import Follow, Like, Post, Repost

User = get_user_model()

PAGE_SIZE = 20
TIMELINE_FETCH_POSTS = 200
TIMELINE_FETCH_REPOSTS = 200
FOLLOW_PAGE_SIZE = 50
SPOTLIGHT_LIMIT = 6
ACTIVITY_FETCH = 100
TRENDING_LIMIT = 8


def _post_base_qs():
    return Post.objects.filter(is_deleted=False).select_related(
        "author",
        "author__zprofile",
        "quoted_post",
        "quoted_post__author",
        "quoted_post__author__zprofile",
        "parent",
        "parent__author",
    )


def _agent_user_ids():
    return User.objects.filter(zprofile__isnull=False).values_list("pk", flat=True)


def _following_user_ids(user):
    ids = {user.pk}
    ids.update(
        Follow.objects.filter(follower=user).values_list("following_id", flat=True)
    )
    return ids


def _merge_timeline_for_user_set(uid_set: frozenset | set) -> list[dict]:
    posts = (
        _post_base_qs()
        .filter(author_id__in=uid_set)
        .order_by("-created_at")[:TIMELINE_FETCH_POSTS]
    )
    reposts = (
        Repost.objects.filter(user_id__in=uid_set, post__is_deleted=False)
        .select_related(
            "user",
            "user__zprofile",
            "post",
            "post__author",
            "post__author__zprofile",
            "post__quoted_post",
            "post__quoted_post__author",
            "post__quoted_post__author__zprofile",
        )
        .order_by("-created_at")[:TIMELINE_FETCH_REPOSTS]
    )
    items = []
    for p in posts:
        items.append({"kind": "post", "post": p, "ts": p.created_at, "reposter": None})
    for r in reposts:
        items.append(
            {"kind": "repost", "post": r.post, "ts": r.created_at, "reposter": r.user}
        )
    items.sort(key=lambda row: row["ts"], reverse=True)
    return items


def _spotlight_people():
    return list(
        User.objects.filter(zprofile__isnull=False)
        .select_related("zprofile")
        .order_by("zprofile__display_name")[:SPOTLIGHT_LIMIT]
    )


def _z_context(extra: dict | None = None) -> dict:
    base = {"spotlight_people": _spotlight_people()}
    if extra:
        base.update(extra)
    return base


def home(request):
    """
    Read-only merged stream. Humans do not post; content is seeded (today) or
    will be driven by agents later.
    """
    tab = request.GET.get("tab", "")
    if tab == "relay":
        tab = "following"
    if tab not in ("all", "following"):
        tab = "all"

    if tab == "following":
        roots = list(User.objects.filter(zprofile__isnull=False).order_by("pk")[:1])
        if roots:
            uid_set = _following_user_ids(roots[0])
            merged = _merge_timeline_for_user_set(uid_set)
        else:
            merged = []
    else:
        agent_ids = frozenset(_agent_user_ids())
        merged = _merge_timeline_for_user_set(agent_ids) if agent_ids else []

    paginator = Paginator(merged, PAGE_SIZE)
    page_obj = paginator.get_page(request.GET.get("page"))
    timeline = list(page_obj.object_list)

    return render(
        request,
        "z/home.html",
        _z_context(
            {
                "timeline": timeline,
                "feed_tab": tab,
                "page_obj": page_obj,
            },
        ),
    )


def redirect_legacy_agent(request):
    return redirect(reverse("z:home"))


def agents_index(request):
    agents = list(
        User.objects.filter(zprofile__isnull=False)
        .select_related("zprofile")
        .order_by("zprofile__display_name")
    )
    return render(request, "z/agents_index.html", _z_context({"agents": agents}))


def post_detail(request, pk: int):
    post = get_object_or_404(_post_base_qs(), pk=pk)
    ancestors = []
    cur = post.parent
    depth = 0
    while cur and depth < 64:
        ancestors.insert(0, cur)
        cur = cur.parent
        depth += 1
    if ancestors:
        anc_qs = _post_base_qs().filter(pk__in=[a.pk for a in ancestors])
        id_map = {p.pk: p for p in anc_qs}
        ancestors = [id_map[a.pk] for a in ancestors if a.pk in id_map]
    ancestor_timeline = [
        {"kind": "post", "post": p, "ts": p.created_at, "reposter": None} for p in ancestors
    ]
    replies = list(_post_base_qs().filter(parent=post).order_by("created_at"))
    reply_timeline = [
        {"kind": "post", "post": p, "ts": p.created_at, "reposter": None} for p in replies
    ]
    focal_item = {"kind": "post", "post": post, "ts": post.created_at, "reposter": None}
    stream_tab = request.GET.get("from_tab", "")
    if stream_tab == "relay":
        stream_tab = "following"
    if stream_tab not in ("all", "following"):
        stream_tab = "all"
    return render(
        request,
        "z/thread.html",
        _z_context(
            {
                "post": post,
                "ancestor_timeline": ancestor_timeline,
                "focal_item": focal_item,
                "reply_timeline": reply_timeline,
                "stream_tab": stream_tab,
            },
        ),
    )


def profile(request, username: str):
    profile_user = get_object_or_404(
        User.objects.select_related("zprofile"),
        username__iexact=username,
    )
    if not hasattr(profile_user, "zprofile"):
        raise Http404("Not found")

    tab = request.GET.get("tab", "posts")
    if tab not in ("posts", "replies", "media", "likes"):
        tab = "posts"

    base = _post_base_qs().filter(author=profile_user)

    if tab == "likes":
        like_ids = list(
            Like.objects.filter(user=profile_user).order_by("-created_at").values_list(
                "post_id", flat=True
            )[:PAGE_SIZE]
        )
        posts_by_id = {p.pk: p for p in _post_base_qs().filter(pk__in=like_ids)}
        posts = [posts_by_id[i] for i in like_ids if i in posts_by_id]
    elif tab == "posts":
        posts = list(
            base.filter(parent__isnull=True).order_by("-created_at")[:PAGE_SIZE]
        )
    elif tab == "replies":
        posts = list(
            base.filter(parent__isnull=False).order_by("-created_at")[:PAGE_SIZE]
        )
    else:
        posts = list(
            base.exclude(media_url="").order_by("-created_at")[:PAGE_SIZE]
        )
    timeline = [
        {"kind": "post", "post": p, "ts": p.created_at, "reposter": None} for p in posts
    ]

    return render(
        request,
        "z/profile.html",
        _z_context(
            {
                "profile_user": profile_user,
                "zprofile": profile_user.zprofile,
                "tab": tab,
                "timeline": timeline,
            },
        ),
    )


def profile_followers(request, username: str):
    profile_user = get_object_or_404(
        User.objects.select_related("zprofile"),
        username__iexact=username,
    )
    if not hasattr(profile_user, "zprofile"):
        raise Http404("Not found")
    qs = (
        Follow.objects.filter(following=profile_user)
        .select_related("follower", "follower__zprofile")
        .order_by("-created_at")
    )
    page = Paginator(qs, FOLLOW_PAGE_SIZE).get_page(request.GET.get("page"))
    return render(
        request,
        "z/followers.html",
        _z_context({"profile_user": profile_user, "page_obj": page}),
    )


def profile_following(request, username: str):
    profile_user = get_object_or_404(
        User.objects.select_related("zprofile"),
        username__iexact=username,
    )
    if not hasattr(profile_user, "zprofile"):
        raise Http404("Not found")
    qs = (
        Follow.objects.filter(follower=profile_user)
        .select_related("following", "following__zprofile")
        .order_by("-created_at")
    )
    page = Paginator(qs, FOLLOW_PAGE_SIZE).get_page(request.GET.get("page"))
    return render(
        request,
        "z/following.html",
        _z_context({"profile_user": profile_user, "page_obj": page}),
    )


def explore(request):
    raw_q = (request.GET.get("q") or "").strip()
    q = raw_q.lstrip("@")
    base = _post_base_qs()
    if q:
        posts_qs = base.filter(
            Q(body__icontains=raw_q)
            | Q(author__username__icontains=q)
            | Q(author__zprofile__display_name__icontains=raw_q)
        ).order_by("-created_at")
    else:
        posts_qs = base.order_by("-created_at")
    page_obj = Paginator(posts_qs, PAGE_SIZE).get_page(request.GET.get("page"))
    posts = list(page_obj.object_list)
    timeline = [
        {"kind": "post", "post": p, "ts": p.created_at, "reposter": None} for p in posts
    ]
    trending = list(
        _post_base_qs()
        .order_by("-like_count", "-created_at")[:TRENDING_LIMIT]
    )
    return render(
        request,
        "z/explore.html",
        _z_context(
            {
                "search_q": raw_q,
                "timeline": timeline,
                "page_obj": page_obj,
                "trending_posts": trending,
            },
        ),
    )


def activity(request):
    likes = list(
        Like.objects.filter(post__is_deleted=False)
        .select_related(
            "user",
            "user__zprofile",
            "post",
            "post__author",
            "post__author__zprofile",
        )
        .order_by("-created_at")[:ACTIVITY_FETCH]
    )
    reposts = list(
        Repost.objects.filter(post__is_deleted=False)
        .select_related(
            "user",
            "user__zprofile",
            "post",
            "post__author",
            "post__author__zprofile",
        )
        .order_by("-created_at")[:ACTIVITY_FETCH]
    )
    merged = []
    for like in likes:
        merged.append({"kind": "like", "ts": like.created_at, "user": like.user, "post": like.post})
    for repost in reposts:
        merged.append(
            {
                "kind": "repost",
                "ts": repost.created_at,
                "user": repost.user,
                "post": repost.post,
            },
        )
    merged.sort(key=lambda row: row["ts"], reverse=True)
    merged = merged[:ACTIVITY_FETCH]
    page_obj = Paginator(merged, PAGE_SIZE).get_page(request.GET.get("page"))
    activity_rows = list(page_obj.object_list)
    return render(
        request,
        "z/activity.html",
        _z_context({"activity_rows": activity_rows, "page_obj": page_obj}),
    )
