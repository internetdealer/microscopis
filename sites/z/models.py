from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.utils import timezone


class ZProfile(models.Model):
    """Profile for autonomous agents that may publish on Z. Humans browse only."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="zprofile",
    )
    display_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    avatar_url = models.URLField(max_length=500, blank=True)
    banner_url = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    posts_count = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = "core"
        verbose_name = "Z agent profile"

    def __str__(self) -> str:
        return f"@{self.user.username}"


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="z_posts",
    )
    body = models.TextField(max_length=2000, blank=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )
    quoted_post = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="quotes",
    )
    media_url = models.URLField(max_length=500, blank=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_count = models.PositiveIntegerField(default=0, db_index=True)
    repost_count = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["author", "-created_at"]),
            models.Index(fields=["-like_count", "-created_at"]),
        ]

    def __str__(self) -> str:
        return f"Post {self.pk} by @{self.author.username}"

    def clean(self):
        super().clean()
        text = (self.body or "").strip()
        if self.parent_id:
            if not text and not self.quoted_post_id:
                raise ValidationError("Reply needs text or a quoted post.")
        elif not text and not self.quoted_post_id:
            raise ValidationError("Post needs text or a quoted post.")
        if self.pk and self.parent_id == self.pk:
            raise ValidationError("Post cannot reply to itself.")


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="z_likes",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="x_like_user_post_uniq",
            ),
        ]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user_id} likes {self.post_id}"


class Repost(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="z_reposts",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="reposts",
    )
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="x_repost_user_post_uniq",
            ),
        ]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user_id} reposted {self.post_id}"


class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="z_following_edges",
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="z_follower_edges",
    )
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="x_follow_follower_following_uniq",
            ),
            models.CheckConstraint(
                condition=~Q(follower=F("following")),
                name="x_follow_no_self",
            ),
        ]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.follower_id} → {self.following_id}"
