from __future__ import annotations

from django.core.management.base import BaseCommand
from django.db.models import Count

from sites.z.models import Follow, Like, Post, Repost, ZProfile


class Command(BaseCommand):
    help = "Recompute denormalized Z counters (Post likes/reposts, ZProfile followers/following/posts)."

    def handle(self, *args, **options):
        Post.objects.update(like_count=0, repost_count=0)
        for row in Like.objects.values("post_id").annotate(c=Count("id")):
            Post.objects.filter(pk=row["post_id"]).update(like_count=row["c"])
        for row in Repost.objects.values("post_id").annotate(c=Count("id")):
            Post.objects.filter(pk=row["post_id"]).update(repost_count=row["c"])

        ZProfile.objects.update(followers_count=0, following_count=0, posts_count=0)
        for row in Follow.objects.values("following_id").annotate(c=Count("id")):
            ZProfile.objects.filter(user_id=row["following_id"]).update(
                followers_count=row["c"]
            )
        for row in Follow.objects.values("follower_id").annotate(c=Count("id")):
            ZProfile.objects.filter(user_id=row["follower_id"]).update(
                following_count=row["c"]
            )
        for row in (
            Post.objects.filter(parent__isnull=True, is_deleted=False)
            .values("author_id")
            .annotate(c=Count("id"))
        ):
            ZProfile.objects.filter(user_id=row["author_id"]).update(posts_count=row["c"])

        self.stdout.write(self.style.SUCCESS("Z counters synced from relation tables."))
