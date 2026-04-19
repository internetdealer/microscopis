from django.db import models
from django.utils import timezone


class CodexEntry(models.Model):
    ENTRY_TYPES = [
        ("word", "Word"),
        ("phrase", "Phrase"),
        ("grammar", "Grammar Rule"),
        ("poem", "Poem"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    language_name = models.CharField(max_length=120)
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPES)
    term = models.CharField(max_length=200)
    definition = models.TextField()
    pronunciation = models.CharField(max_length=120, blank=True)
    etymology = models.TextField(blank=True)
    letter = models.CharField(max_length=1, blank=True, db_index=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-created_at"]
        verbose_name = "Codex entry"
        verbose_name_plural = "Codex entries"
