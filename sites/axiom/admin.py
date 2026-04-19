from django.contrib import admin

from sites.axiom.models import AxiomLaw


@admin.register(AxiomLaw)
class AxiomLawAdmin(admin.ModelAdmin):
    list_display = ("title", "instrument_name", "law_type", "is_featured", "enacted_at")
    list_filter = ("law_type", "is_featured")
    search_fields = ("title", "civilization_name", "body")

    @admin.display(description="Instrument")
    def instrument_name(self, obj):
        return obj.civilization_name

    prepopulated_fields = {"slug": ("title",)}
