from django.db import models


class WebsiteContent(models.Model):
    site_slug = models.SlugField(max_length=255, db_index=True)
    page_slug = models.SlugField(max_length=255, default="home", db_index=True)
    title = models.CharField(max_length=512, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["site_slug", "page_slug", "id"]

    def __str__(self) -> str:
        return f"{self.site_slug}/{self.page_slug}: {self.title or self.content[:40]}"
