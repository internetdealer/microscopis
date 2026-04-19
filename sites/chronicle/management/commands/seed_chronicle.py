from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.utils.bulk_generators import chronicle_generated_entries
from core.utils.image_urls import ensure_reachable_image_url
from sites.chronicle.models import ChronicleEntry, ChronicleTag
from sites.chronicle.seed_data import ENTRIES, TAGS

TARGET_ENTRIES = 100


def _dt(tup: tuple[int, ...]) -> datetime:
    y, m, d, h, mi = tup
    dt = datetime(y, m, d, h, mi)
    return timezone.make_aware(dt, timezone.get_current_timezone())


class Command(BaseCommand):
    help = "Load Chronicle tags and entries (replaces existing rows)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--verify-images",
            action="store_true",
            help="HTTP-check hero and avatar image URLs; substitute fallbacks if unreachable (slower).",
        )

    def handle(self, *args, **options):
        verify = options.get("verify_images")
        warn = (
            (lambda m: self.stdout.write(self.style.WARNING(m))) if verify else None
        )

        with transaction.atomic():
            ChronicleEntry.objects.all().delete()
            ChronicleTag.objects.all().delete()

            tag_map: dict[str, ChronicleTag] = {}
            for t in TAGS:
                tag_map[t["slug"]] = ChronicleTag.objects.create(slug=t["slug"], name=t["name"])

            base = list(ENTRIES)
            extra = max(0, TARGET_ENTRIES - len(base))
            all_entries = base + chronicle_generated_entries(len(base), extra)

            n = 0
            for raw in all_entries:
                tag_slugs = raw["tags"]
                pub_tuple = raw["published_at"]
                hero = raw["image_url"]
                avatar = raw["author_avatar_url"]
                if verify:
                    hero = ensure_reachable_image_url(hero, warn)
                    avatar = ensure_reachable_image_url(avatar, warn)
                data = {
                    "slug": raw["slug"],
                    "title": raw["title"],
                    "excerpt": raw["excerpt"],
                    "body": raw["body"],
                    "author_name": raw["author_name"],
                    "author_handle": raw["author_handle"],
                    "author_avatar_url": avatar,
                    "mood": raw["mood"],
                    "mood_emoji": raw["mood_emoji"],
                    "current_music": raw["current_music"],
                    "location": raw["location"],
                    "published_at": _dt(pub_tuple),
                    "image_url": hero,
                    "image_credit": raw["image_credit"],
                    "display_likes": raw["display_likes"],
                }
                entry = ChronicleEntry.objects.create(**data)
                entry.tags.set([tag_map[s] for s in tag_slugs])
                n += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Chronicle: {len(tag_map)} tags, {n} entries loaded."
            )
        )
