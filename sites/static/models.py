from django.db import models
from django.utils import timezone


class StaticSignal(models.Model):
    SIGNAL_TYPES = [
        ("numbers", "Numbers Station"),
        ("broadcast", "Broadcast"),
        ("deep_space", "Deep Space"),
        ("unknown", "Unknown"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    designation = models.CharField(max_length=80)
    signal_type = models.CharField(max_length=20, choices=SIGNAL_TYPES)
    origin_description = models.CharField(max_length=200, blank=True)
    transcript = models.TextField()
    analysis_notes = models.TextField(blank=True)
    audio_url = models.URLField(max_length=500, blank=True)
    archive_embed_id = models.CharField(
        max_length=80,
        blank=True,
        help_text="Internet Archive item id for embedded player, e.g. ird059 → archive.org/embed/ird059",
    )
    archive_embed_file = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional file inside the item (e.g. tcp_d1_01_track.mp3) to start that track in the embed.",
    )
    is_featured = models.BooleanField(default=False, db_index=True)
    intercepted_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-intercepted_at"]
        verbose_name = "Static signal"
