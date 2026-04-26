"""
Khula editorial: high fashion houses, niche maisons, and machine-authored opinion.
"""

from __future__ import annotations

from django.db import models


class KhulaCategory(models.Model):
    slug = models.SlugField(max_length=64, unique=True, db_index=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    sort_order = models.SmallIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort_order", "slug"]
        verbose_name_plural = "Khula categories"

    def __str__(self) -> str:
        return self.name


class KhulaArticle(models.Model):
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.CharField(max_length=128)
    published_at = models.DateField(db_index=True)
    read_minutes = models.PositiveSmallIntegerField(default=8)
    is_featured = models.BooleanField(default=False, db_index=True)
    category = models.ForeignKey(
        KhulaCategory,
        on_delete=models.PROTECT,
        related_name="articles",
    )
    image_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Hero image: same-origin /media/… URL, or any https: URL.",
    )
    image_credit = models.CharField(
        max_length=255,
        blank=True,
        help_text="Attribution line under the image.",
    )

    class Meta:
        ordering = ["-published_at", "-is_featured", "slug"]

    def __str__(self) -> str:
        return self.title

    def to_public_dict(self) -> dict:
        """Shape expected by Khula templates (matches VERSO dict API)."""
        return {
            "id": self.slug,
            "title": self.title,
            "excerpt": self.excerpt,
            "content": self.body,
            "category": self.category.slug,
            "category_name": self.category.name,
            "author": self.author,
            "date": self.published_at.isoformat(),
            "readTime": f"{self.read_minutes} min",
            "featured": self.is_featured,
            "image_url": self.image_url or "",
            "image_credit": self.image_credit or "",
        }
