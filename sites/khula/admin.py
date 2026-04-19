from django.contrib import admin

from sites.khula.models import KhulaArticle, KhulaCategory


@admin.register(KhulaCategory)
class KhulaCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "sort_order")
    ordering = ("sort_order", "slug")


@admin.register(KhulaArticle)
class KhulaArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "published_at", "is_featured")
    fields = (
        "slug",
        "title",
        "excerpt",
        "body",
        "author",
        "published_at",
        "read_minutes",
        "is_featured",
        "category",
        "image_url",
        "image_credit",
    )
    list_filter = ("category", "is_featured", "published_at")
    search_fields = ("title", "slug", "excerpt", "author")
    ordering = ("-published_at",)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
