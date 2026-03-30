"""
Chronicle read-only journal archive. Entries are stored in the database; site visitors
cannot submit posts or comments (views expose only GET routes).
"""

from __future__ import annotations

from django.db import models


class ChronicleTag(models.Model):
    slug = models.SlugField(max_length=64, unique=True, db_index=True)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class ChronicleEntry(models.Model):
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    author_name = models.CharField(max_length=128)
    author_handle = models.SlugField(max_length=64, db_index=True)
    author_avatar_url = models.URLField(max_length=500, blank=True)
    mood = models.CharField(max_length=64, blank=True)
    mood_emoji = models.CharField(max_length=24, blank=True)
    current_music = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    published_at = models.DateTimeField(db_index=True)
    image_url = models.URLField(max_length=500, blank=True)
    image_credit = models.CharField(max_length=255, blank=True)
    display_likes = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(ChronicleTag, related_name="entries", blank=True)

    class Meta:
        ordering = ["-published_at", "slug"]

    def __str__(self) -> str:
        return self.title
