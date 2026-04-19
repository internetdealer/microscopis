from django.db import models
from django.utils import timezone


class SableTheory(models.Model):
    PLAUSIBILITY = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("unsettling", "Unsettlingly High"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    plausibility = models.CharField(
        max_length=20,
        choices=PLAUSIBILITY,
        default="medium",
    )
    body = models.TextField()
    evidence_cited = models.TextField(blank=True)
    real_events = models.TextField(blank=True)
    wikipedia_urls = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    published_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-published_at"]
        verbose_name = "Sable theory"
        verbose_name_plural = "Sable theories"
