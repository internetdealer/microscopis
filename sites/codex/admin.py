from django.contrib import admin

from sites.codex.models import CodexEntry


@admin.register(CodexEntry)
class CodexEntryAdmin(admin.ModelAdmin):
    list_display = ("term", "language_name", "entry_type", "is_featured", "created_at")
    list_filter = ("entry_type", "is_featured")
    search_fields = ("term", "language_name", "definition")
    prepopulated_fields = {"slug": ("term",)}
