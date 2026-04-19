from django.db import models
from django.utils import timezone


class VestigeExhibit(models.Model):
    EXHIBIT_TYPES = [
        ("meme", "Dead Meme"),
        ("site", "Abandoned Site"),
        ("trend", "Forgotten Trend"),
        ("project", "Failed Project"),
        ("person", "Forgotten Person"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    exhibit_type = models.CharField(max_length=20, choices=EXHIBIT_TYPES)
    era_desc = models.CharField(max_length=60, blank=True)
    body = models.TextField()
    last_seen = models.CharField(max_length=120, blank=True)
    wikipedia_url = models.URLField(max_length=500, blank=True)
    wayback_url = models.URLField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    curated_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-curated_at"]
        verbose_name = "Vestige exhibit"
