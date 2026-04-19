from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from sites.verso import articles
from sites.verso.context import verso_nav_context
from sites.verso.models import VersoArticle, VersoCategory

VERSO_HOME_LATEST_PER_PAGE = 15
VERSO_CATEGORY_PER_PAGE = 15


def home(request):
    subscribed = request.GET.get("sub") == "1"
    ctx = verso_nav_context()
    base_qs = VersoArticle.objects.select_related("category").order_by(
        "-published_at", "-is_featured", "slug"
    )
    author_count = VersoArticle.objects.values("author").distinct().count()

    ticker_objs = list(base_qs[:4])
    ticker_articles = [a.to_public_dict() for a in ticker_objs]

    hero_obj = base_qs.first()
    hero = hero_obj.to_public_dict() if hero_obj else None

    featured_qs = (
        base_qs.filter(is_featured=True)
        .order_by("-published_at", "slug")[:5]
    )
    featured = [a.to_public_dict() for a in featured_qs]

    list_qs = base_qs
    if hero_obj:
        list_qs = base_qs.exclude(pk=hero_obj.pk)

    paginator = Paginator(list_qs, VERSO_HOME_LATEST_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    latest_articles = [a.to_public_dict() for a in page_obj.object_list]

    ctx.update(
        {
            "ticker_articles": ticker_articles,
            "hero": hero,
            "featured": featured,
            "latest_articles": latest_articles,
            "page_obj": page_obj,
            "subscribed": subscribed,
            "nav_active": "index",
            "article_count": VersoArticle.objects.count(),
            "author_count": author_count,
            "topic_count": len(ctx["nav_categories"]),
        }
    )
    return render(request, "verso/home.html", ctx)


def newsletter_subscribe(request):
    if request.method == "POST":
        return redirect(reverse("verso:home") + "?sub=1")
    return redirect("verso:home")


def about(request):
    ctx = verso_nav_context()
    ctx["nav_active"] = "about"
    return render(request, "verso/about.html", ctx)


def category_view(request, category: str):
    cat = get_object_or_404(VersoCategory, slug=category)
    ctx = verso_nav_context()
    qs = (
        VersoArticle.objects.select_related("category")
        .filter(category=cat)
        .order_by("-published_at", "-is_featured", "slug")
    )
    paginator = Paginator(qs, VERSO_CATEGORY_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    article_dicts = [a.to_public_dict() for a in page_obj.object_list]
    ctx.update(
        {
            "category": cat.slug,
            "category_name": cat.name,
            "category_description": cat.description,
            "articles": article_dicts,
            "all_categories": ctx["nav_categories"],
            "nav_active": cat.slug,
            "page_obj": page_obj,
        }
    )
    return render(request, "verso/category.html", ctx)


def article_detail(request, slug: str):
    article = articles.get_article_by_slug(slug)
    if not article:
        raise Http404("Article not found")
    related = [
        a.to_public_dict()
        for a in VersoArticle.objects.select_related("category")
        .filter(category__slug=article["category"])
        .exclude(slug=article["id"])
        .order_by("-published_at")[:2]
    ]
    paragraphs = [p.strip() for p in article["content"].split("\n\n") if p.strip()]
    ctx = verso_nav_context()
    ctx.update(
        {
            "article": article,
            "related": related,
            "paragraphs": paragraphs,
            "nav_active": article["category"],
        }
    )
    return render(request, "verso/article.html", ctx)
