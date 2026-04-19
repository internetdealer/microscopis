from django.contrib import admin

from sites.residue.models import ResidueFragment


@admin.register(ResidueFragment)
class ResidueFragmentAdmin(admin.ModelAdmin):
    list_display = ("site_name", "fragment_type", "is_featured", "archived_at")
    list_filter = ("fragment_type", "is_featured")
    search_fields = ("site_name", "recovered_text")
    prepopulated_fields = {"slug": ("site_name",)}
