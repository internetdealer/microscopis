from django.db import models
from django.utils import timezone


class ParlorDialogue(models.Model):
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    person_a = models.CharField(max_length=120)
    person_b = models.CharField(max_length=120)
    body = models.TextField(help_text="Full dialogue text, paragraphs separated by blank lines.")
    is_featured = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-created_at"]
        verbose_name = "Parlor dialogue"
