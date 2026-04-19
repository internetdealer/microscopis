from django.contrib import admin

from sites.parlor.models import ParlorDialogue


@admin.register(ParlorDialogue)
class ParlorDialogueAdmin(admin.ModelAdmin):
    list_display = ("title", "person_a", "person_b", "is_featured", "created_at")
    list_filter = ("is_featured",)
    search_fields = ("title", "person_a", "person_b", "body")
    prepopulated_fields = {"slug": ("title",)}
