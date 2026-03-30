from django.db import models


class SearchIndex(models.Model):
    website_name = models.CharField(max_length=255)
    website_slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    topic = models.CharField(max_length=128, db_index=True)
    is_featured = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["website_name"]

    def __str__(self) -> str:
        return self.website_name
