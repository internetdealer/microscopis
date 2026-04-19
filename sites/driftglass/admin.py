from django.contrib import admin

from sites.driftglass.models import DriftglassImage


@admin.register(DriftglassImage)
class DriftglassImageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "probe_agent", "is_featured", "created_at")
    list_filter = ("is_featured", "probe_agent", "created_at")
    search_fields = ("title", "slug", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    fieldsets = (
        (None, {"fields": ("slug", "title", "description")}),
        ("Asset", {"fields": ("image_url", "image_credit", "source_host")}),
        ("Telemetry", {"fields": ("probe_agent", "is_featured", "created_at")}),
    )
    readonly_fields = ()
