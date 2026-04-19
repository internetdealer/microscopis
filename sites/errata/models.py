from django.db import models
from django.utils import timezone


class ErrataCorrection(models.Model):
    SEVERITY = [
        ("minor", "Minor"),
        ("major", "Major"),
        ("critical", "Critical"),
        ("retraction", "Full Retraction"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    original_claim = models.CharField(max_length=300)
    correction = models.TextField()
    severity = models.CharField(
        max_length=20, choices=SEVERITY, default="minor"
    )
    source_cited = models.CharField(max_length=200, blank=True)
    editor_note = models.TextField(blank=True)
    fact_year = models.IntegerField(null=True, blank=True, db_index=True)
    wikipedia_url = models.URLField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    issued_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-issued_at"]
        verbose_name = "Errata correction"
