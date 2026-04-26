"""
Fetch many articles from configured RSS/Atom feeds into :class:`core.models.IngestedArticle`
(``INGEST_OMNI_POOL``). Run before ``seed_microscopis`` for web-sourced content.
"""

from __future__ import annotations

import time
from pathlib import Path

import feedparser
import yaml
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from core.models import IngestedArticle
from core.utils.ingest_fetch import _norm_body_hash, extract_article_from_url

DEFAULT_CONFIG = (
    settings.BASE_DIR / "config" / "web_ingest" / "feeds.yaml"
)


def _load_yaml(p: Path) -> dict:
    if not p.is_file():
        raise CommandError(f"Missing config: {p}")
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


class Command(BaseCommand):
    help = "Ingest RSS-linked articles trafilatura → IngestedArticle (see config/web_ingest/feeds.yaml)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--config",
            type=str,
            default="",
            help=f"YAML path (default: {DEFAULT_CONFIG})",
        )
        parser.add_argument(
            "--sleep",
            type=float,
            default=0.35,
            help="Delay between page fetches (seconds).",
        )
        parser.add_argument(
            "--max-total",
            type=int,
            default=0,
            help="Override max_total_articles in config (0 = use config).",
        )

    def handle(self, *args, **options):
        p = Path(options["config"] or DEFAULT_CONFIG)
        data = _load_yaml(p)
        pool = (data.get("pool") or "omni").strip()
        max_total = int(
            options["max_total"] or data.get("max_total_articles", 2000) or 2000
        )
        per_feed = int(data.get("max_entries_per_feed", 40) or 40)
        min_body = int(data.get("min_body_chars", 200) or 200)
        feeds = data.get("feeds") or []
        if not isinstance(feeds, list) or not feeds:
            raise CommandError("config feeds: list of {url, name} is required")
        sl = float(options["sleep"] or 0.35)

        added = 0
        seen_hash: set[str] = set(
            IngestedArticle.objects.values_list("content_hash", flat=True)
        )

        for block in feeds:
            if max_total and added >= max_total:
                break
            furl = (block.get("url") or "").strip()
            label = (block.get("name") or furl)[:400]
            if not furl:
                continue
            self.stdout.write(f"Feed: {label}")
            try:
                fp = feedparser.parse(furl)
            except (OSError, ValueError) as e:
                self.stdout.write(self.style.WARNING(f"  skip (parse): {e}"))
                continue
            for ent in (getattr(fp, "entries", None) or [])[:per_feed]:
                if max_total and added >= max_total:
                    break
                link = (getattr(ent, "link", None) or "").strip() or (getattr(ent, "id", None) or "")
                if not link.startswith("http"):
                    continue
                if IngestedArticle.objects.filter(source_url=link).exists():
                    continue
                time.sleep(sl)
                payload = extract_article_from_url(link)
                if not payload:
                    continue
                ch = _norm_body_hash(payload.get("body"))
                if ch in seen_hash:
                    continue
                if len((payload.get("body") or "").strip()) < min_body:
                    continue
                IngestedArticle.objects.create(
                    source_url=link[:2000],
                    pool=pool,
                    title=(payload.get("title") or "Untitled")[:500],
                    body=payload["body"],
                    excerpt=(payload.get("excerpt") or "")[:2000],
                    author_line=(payload.get("author_line") or "")[:400],
                    published_at=payload.get("published_at"),
                    image_media_relpath=(payload.get("image_media_relpath") or "")[:500],
                    image_credit=(payload.get("image_credit") or "Source")[:500],
                    content_hash=ch,
                    feed_label=label,
                    source_image_url=(payload.get("source_image_url") or "")[:2000],
                )
                seen_hash.add(ch)
                added += 1
                if added % 20 == 0:
                    self.stdout.write(f"  ingested: {added}")

        self.stdout.write(self.style.SUCCESS(f"Done. New rows (this run’s additions): {added} total in pool {pool!r}."))
        c = IngestedArticle.objects.filter(pool=pool).count()
        self.stdout.write(f"Total IngestedArticle in pool: {c}")
