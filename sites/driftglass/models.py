"""Remote image probes — DB tables remain under the ``core`` app (historical migrations)."""

from __future__ import annotations

from django.db import models
from django.utils import timezone


class DriftglassImage(models.Model):
    """A fetched remote image plus agent-generated copy."""

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    image_credit = models.CharField(
        max_length=255,
        blank=True,
        help_text="Attribution line (e.g. Unsplash photographer).",
    )
    source_host = models.CharField(
        max_length=120,
        blank=True,
        help_text="Origin host label for telemetry (e.g. images.unsplash.com).",
    )
    probe_agent = models.CharField(
        max_length=64,
        default="fetch-agent-v3",
        help_text="Synthetic agent id shown in the UI.",
    )
    is_featured = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-created_at", "slug"]
        verbose_name = "Driftglass image"
        verbose_name_plural = "Driftglass images"

    def __str__(self) -> str:
        return self.title
