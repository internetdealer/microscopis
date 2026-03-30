from django.contrib import admin

from core.models.search_models import SearchIndex


class SearchIndexAdmin(admin.ModelAdmin):
    list_display = ("website_name", "website_slug", "topic", "is_featured")
    list_filter = ("is_featured", "topic")
    search_fields = ("website_name", "website_slug", "description", "topic")
