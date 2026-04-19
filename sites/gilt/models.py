from django.db import models
from django.utils import timezone


class GiltEntry(models.Model):
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    billionaire_name = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    body = models.TextField()
    mood_tag = models.CharField(max_length=40, blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    entry_date = models.DateField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-entry_date"]
        verbose_name = "Gilt diary entry"
        verbose_name_plural = "Gilt diary entries"
