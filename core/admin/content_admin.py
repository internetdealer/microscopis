from django.contrib import admin

from core.models.content_models import WebsiteContent


class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ("site_slug", "page_slug", "title", "updated_at")
    list_filter = ("site_slug", "page_slug")
    search_fields = ("title", "content", "site_slug")
