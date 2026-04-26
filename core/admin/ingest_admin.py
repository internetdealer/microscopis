from django.contrib import admin

from core.models.ingest_models import IngestedArticle


@admin.register(IngestedArticle)
class IngestedArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pool", "fetched_at", "source_url")
    list_filter = ("pool", "fetched_at")
    search_fields = ("title", "source_url", "feed_label")
    readonly_fields = ("fetched_at", "content_hash")
