from django.contrib import admin

from sites.z.models import Follow, Like, Post, Repost, ZProfile


@admin.register(ZProfile)
class ZProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "display_name", "created_at")
    search_fields = ("user__username", "display_name", "bio")
    raw_id_fields = ("user",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "body_preview", "parent_id", "created_at", "is_deleted")
    list_filter = ("is_deleted", "edited")
    search_fields = ("body", "author__username")
    raw_id_fields = ("author", "parent", "quoted_post")

    @admin.display(description="Body")
    def body_preview(self, obj):
        return (obj.body or "")[:60]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    raw_id_fields = ("user", "post")


@admin.register(Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    raw_id_fields = ("user", "post")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "following", "created_at")
    raw_id_fields = ("follower", "following")
