from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from core.utils.bulk_generators import chronicle_generated_entries
from core.utils.synthetic_media import generate_chronicle_avatar, generate_chronicle_hero
from core.utils.web_seed import take_ingested_for_site
from sites.chronicle.models import ChronicleEntry, ChronicleTag
from sites.chronicle.seed_data import ENTRIES, TAGS

TARGET_ENTRIES = 100


def _dt(tup: tuple[int, ...]) -> datetime:
    y, m, d, h, mi = tup
    dt = datetime(y, m, d, h, mi)
    return timezone.make_aware(dt, timezone.get_current_timezone())


class Command(BaseCommand):
    help = "Load Chronicle tags and entries (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ChronicleEntry.objects.all().delete()
            ChronicleTag.objects.all().delete()

            tag_map: dict[str, ChronicleTag] = {}
            for t in TAGS:
                tag_map[t["slug"]] = ChronicleTag.objects.create(
                    slug=t["slug"], name=t["name"]
                )
            tag_slugs = [t["slug"] for t in TAGS]
            b = take_ingested_for_site("chronicle", n=TARGET_ENTRIES)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    raw = ingest_mapping.chronicle_entry(ing, i, tag_slugs)
                    avatar, _ = generate_chronicle_avatar(
                        raw["author_handle"],
                        entry_title=raw.get("title", "")[:200],
                    )
                    tgs = raw.pop("tags")
                    pub = raw["published_at"]
                    if timezone.is_naive(pub):
                        pub = timezone.make_aware(pub, timezone.get_current_timezone())
                    raw["published_at"] = pub
                    raw["author_avatar_url"] = avatar
                    entry = ChronicleEntry.objects.create(**raw)
                    entry.tags.set([tag_map[s] for s in tgs])
                    n += 1
            else:
                base = list(ENTRIES)
                extra = max(0, TARGET_ENTRIES - len(base))
                all_entries = base + chronicle_generated_entries(len(base), extra)
                for raw in all_entries:
                    tag_s = raw["tags"]
                    pub_tuple = raw["published_at"]
                    tag0 = tag_s[0] if tag_s else "agents"
                    ex_hero = (raw.get("image_url") or "").strip()
                    if ex_hero:
                        hero, hcred = ex_hero, (raw.get("image_credit") or "").strip() or "Image"
                    else:
                        hero, hcred = generate_chronicle_hero(
                            raw["slug"],
                            primary_tag=tag0,
                            title=raw.get("title", ""),
                            excerpt=raw.get("excerpt", ""),
                        )
                    avatar, _ = generate_chronicle_avatar(
                        raw["author_handle"],
                        entry_title=raw.get("title", ""),
                    )
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
                        "image_credit": hcred,
                        "display_likes": raw["display_likes"],
                    }
                    entry = ChronicleEntry.objects.create(**data)
                    entry.tags.set([tag_map[s] for s in tag_s])
                    n += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Chronicle: {len(tag_map)} tags, {n} entries loaded."
            )
        )
