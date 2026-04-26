"""
Canonical store for `ingest_web_corpus`: one row per fetched source URL, shared across site seeds.
"""

from __future__ import annotations

from django.db import models


class IngestedArticle(models.Model):
    """
    Fetched main text and hero image (under MEDIA) for re-seed idempotency. ``pool`` groups feeds
    so each site can select rows (see ``core/ingest/pools``).
    """

    source_url = models.CharField(
        max_length=2000, unique=True, db_index=True, help_text="Original article / page URL"
    )
    pool = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Logical group from feeds.yaml (e.g. tech, fashion, longform, news, culture).",
    )
    title = models.CharField(max_length=500)
    body = models.TextField(help_text="Plain extracted main text")
    excerpt = models.TextField(blank=True)
    author_line = models.CharField(max_length=400, blank=True)
    published_at = models.DateTimeField(null=True, blank=True, db_index=True)
    # Path inside MEDIA root, e.g. sourced/ingest/a1b2c3d4e5f6/hero.jpg — see synthetic_media.public_url_for_path
    image_media_relpath = models.CharField(max_length=500, blank=True)
    image_credit = models.CharField(max_length=500, blank=True)
    content_hash = models.CharField(
        max_length=64, db_index=True, help_text="sha256 of normalized body for deduplication"
    )
    feed_label = models.CharField(
        max_length=400, blank=True, help_text="Source feed or file label (debugging only)"
    )
    fetched_at = models.DateTimeField(auto_now_add=True, db_index=True)
    # Image URL used before local save (or og:url); optional
    source_image_url = models.CharField(max_length=2000, blank=True)

    class Meta:
        ordering = ["id"]
        app_label = "core"
        verbose_name = "Ingested article"
        verbose_name_plural = "Ingested articles"

    def __str__(self) -> str:
        return self.title[:80]
