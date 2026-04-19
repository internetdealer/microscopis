from django.contrib import admin

from sites.vestige.models import VestigeExhibit


@admin.register(VestigeExhibit)
class VestigeExhibitAdmin(admin.ModelAdmin):
    list_display = ("title", "exhibit_type", "era_desc", "is_featured", "curated_at")
    list_filter = ("exhibit_type", "is_featured")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
