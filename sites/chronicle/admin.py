from django.contrib import admin

from sites.chronicle.models import ChronicleEntry, ChronicleTag


@admin.register(ChronicleTag)
class ChronicleTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ChronicleEntry)
class ChronicleEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author_handle", "published_at")
    list_filter = ("published_at", "author_handle")
    search_fields = ("title", "slug", "body", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    date_hierarchy = "published_at"
