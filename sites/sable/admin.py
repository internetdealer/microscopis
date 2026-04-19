from django.contrib import admin

from sites.sable.models import SableTheory


@admin.register(SableTheory)
class SableTheoryAdmin(admin.ModelAdmin):
    list_display = ("title", "plausibility", "is_featured", "published_at")
    list_filter = ("plausibility", "is_featured")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
