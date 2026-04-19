from django.contrib import admin

from sites.static.models import StaticSignal


@admin.register(StaticSignal)
class StaticSignalAdmin(admin.ModelAdmin):
    list_display = (
        "designation",
        "signal_type",
        "archive_embed_id",
        "is_featured",
        "intercepted_at",
    )
    list_filter = ("signal_type", "is_featured")
    search_fields = ("designation", "transcript", "archive_embed_id")
    prepopulated_fields = {"slug": ("designation",)}
