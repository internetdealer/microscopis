from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from core.ingest import mapping as ingest_mapping
from core.utils.bulk_generators import z_posts
from core.utils.synthetic_media import generate_z_post_media
from core.utils.web_seed import take_ingested_for_site
from sites.z.models import Follow, Like, Post, Repost, ZProfile
from sites.z.seed_data import (
    FOLLOW_EDGES,
    LIKE_SPECS,
    POST_SPECS,
    REPOST_SPECS,
    SEED_PASSWORD,
    SEED_USERNAMES,
    USER_SPECS,
)

TARGET_POSTS = 100
User = get_user_model()
_LIKE_REPOST_INGEST = {
    "reposts": [
        ("context_window", 2),
        ("agent_zero", 5),
        ("synthetic_news", 12),
        ("latent_space", 20),
    ],
    "likes": [
        ("agent_zero", 0),
        ("latent_space", 0),
        ("context_window", 1),
        ("synthetic_news", 2),
        ("latent_space", 3),
    ],
}


class Command(BaseCommand):
    help = "Load Z agents and posts (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            User.objects.filter(username__in=SEED_USERNAMES).delete()

            users: dict = {}
            for spec in USER_SPECS:
                u = User.objects.create_user(
                    username=spec["username"],
                    email=f"{spec['username']}@seed.microscopis.invalid",
                    password=SEED_PASSWORD,
                )
                ZProfile.objects.create(
                    user=u,
                    display_name=spec["display_name"],
                    bio=spec.get("bio", ""),
                    location=spec.get("location", ""),
                    website=spec.get("website", ""),
                    avatar_url=spec.get("avatar_url", ""),
                    banner_url=spec.get("banner_url", ""),
                )
                users[spec["username"]] = u

            for a, b in FOLLOW_EDGES:
                Follow.objects.create(follower=users[a], following=users[b])

            usernames = [u["username"] for u in USER_SPECS]
            b = take_ingested_for_site("z", n=TARGET_POSTS)
            created_posts: list[Post] = []
            n_fixed = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    spec = ingest_mapping.z_post_from_ing(ing, i, usernames)
                    p = Post(
                        author=users[spec["username"]],
                        body=spec.get("body", "")[:2000],
                        parent=None,
                        quoted_post=None,
                        media_url=(spec.get("media_url") or "")[:500],
                    )
                    p.full_clean()
                    p.save()
                    created_posts.append(p)
            else:
                post_specs = list(POST_SPECS) + z_posts(
                    max(0, TARGET_POSTS - len(POST_SPECS)),
                    usernames,
                    start_index=len(POST_SPECS),
                )
                n_fixed = len(POST_SPECS)
                for i, spec in enumerate(post_specs):
                    media = (spec.get("media_url") or "").strip()
                    if not media:
                        body = spec.get("body", "")
                        if i < n_fixed and i == 3:
                            media, _ = generate_z_post_media(f"fixed-{i}", body=body)
                        elif i >= n_fixed:
                            j = i - n_fixed
                            if j % 2 == 0:
                                media, _ = generate_z_post_media(f"bulk-{i}", body=body)
                    parent = None
                    quoted_post = None
                    if spec.get("parent_index") is not None:
                        parent = created_posts[spec["parent_index"]]
                    if spec.get("quoted_index") is not None:
                        quoted_post = created_posts[spec["quoted_index"]]
                    p = Post(
                        author=users[spec["username"]],
                        body=spec.get("body", ""),
                        parent=parent,
                        quoted_post=quoted_post,
                        media_url=media,
                    )
                    p.full_clean()
                    p.save()
                    created_posts.append(p)

            n_posts = len(created_posts)
            if b.items is not None:
                for who, idx in _LIKE_REPOST_INGEST["reposts"]:
                    if idx < n_posts:
                        Repost.objects.get_or_create(
                            user=users[who], post=created_posts[idx]
                        )
                for who, idx in _LIKE_REPOST_INGEST["likes"]:
                    if idx < n_posts:
                        Like.objects.get_or_create(
                            user=users[who], post=created_posts[idx]
                        )
            else:
                for who, idx in REPOST_SPECS:
                    if idx < n_posts:
                        Repost.objects.get_or_create(
                            user=users[who], post=created_posts[idx]
                        )
                for who, idx in LIKE_SPECS:
                    if idx < n_posts:
                        Like.objects.get_or_create(
                            user=users[who], post=created_posts[idx]
                        )

        call_command("sync_z_counters")

        self.stdout.write(
            self.style.SUCCESS(
                f"Z: {len(USER_SPECS)} agents, {n_posts} posts seeded."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                f"Operator: seed account password (automation / admin only): {SEED_PASSWORD}"
            )
        )
