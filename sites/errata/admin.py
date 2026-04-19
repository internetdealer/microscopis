from django.contrib import admin

from sites.errata.models import ErrataCorrection


@admin.register(ErrataCorrection)
class ErrataCorrectionAdmin(admin.ModelAdmin):
    list_display = ("slug", "severity", "is_featured", "issued_at")
    list_filter = ("severity", "is_featured")
    search_fields = ("original_claim", "correction")
