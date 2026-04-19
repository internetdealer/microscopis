from django.contrib import admin

from sites.gilt.models import GiltEntry


@admin.register(GiltEntry)
class GiltEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "billionaire_name", "mood_tag", "is_featured", "entry_date")
    list_filter = ("is_featured", "entry_date")
    search_fields = ("title", "billionaire_name", "body")
    prepopulated_fields = {"slug": ("title",)}
