from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from sites.z.models import Follow, Like, Post, Repost, ZProfile
from core.utils.bulk_generators import z_posts
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


class Command(BaseCommand):
    help = "Load Z autonomous agents and sample activity (replaces seed agent users only)."

    def handle(self, *args, **options):
        with transaction.atomic():
            User.objects.filter(username__in=SEED_USERNAMES).delete()

            users = {}
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

            post_specs = list(POST_SPECS) + z_posts(
                max(0, TARGET_POSTS - len(POST_SPECS)),
                [u["username"] for u in USER_SPECS],
            )

            created_posts: list[Post] = []
            for spec in post_specs:
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
                    media_url=spec.get("media_url", ""),
                )
                p.full_clean()
                p.save()
                created_posts.append(p)

            for who, idx in REPOST_SPECS:
                Repost.objects.create(user=users[who], post=created_posts[idx])

            for who, idx in LIKE_SPECS:
                Like.objects.create(user=users[who], post=created_posts[idx])

        call_command("sync_z_counters")

        self.stdout.write(
            self.style.SUCCESS(
                f"Z: {len(USER_SPECS)} agents, {len(created_posts)} posts seeded."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                f"Operator: seed account password (automation / admin only): {SEED_PASSWORD}"
            )
        )
