from django.db import models
from django.utils import timezone


class ResidueFragment(models.Model):
    FRAGMENT_TYPES = [
        ("page", "Webpage"),
        ("post", "Blog Post"),
        ("comment", "Comment"),
        ("profile", "Profile"),
        ("listing", "Listing"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    original_url = models.CharField(max_length=300)
    fragment_type = models.CharField(max_length=20, choices=FRAGMENT_TYPES)
    site_name = models.CharField(max_length=120)
    recovered_text = models.TextField()
    context_notes = models.TextField(blank=True)
    wayback_url = models.URLField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    archived_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-archived_at"]
        verbose_name = "Residue fragment"
