from __future__ import annotations

from django.db import transaction
from django.db.models import F
from django.db.models.functions import Greatest
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_save

from sites.z.models import Follow, Like, Post, Repost


@receiver(pre_save, sender=Post)
def _post_track_prev_root_live(sender, instance: Post, **kwargs):
    if kwargs.get("raw"):
        return
    if instance.pk:
        try:
            old = Post.objects.only("parent_id", "is_deleted").get(pk=instance.pk)
            instance._z_prev_root_live = old.parent_id is None and not old.is_deleted
        except Post.DoesNotExist:
            instance._z_prev_root_live = False
    else:
        instance._z_prev_root_live = False


def _adjust_author_posts_count(author_id: int, delta: int) -> None:
    if not author_id or not delta:
        return
    from sites.z.models import ZProfile

    if delta > 0:
        ZProfile.objects.filter(user_id=author_id).update(posts_count=F("posts_count") + delta)
    else:
        ZProfile.objects.filter(user_id=author_id).update(
            posts_count=Greatest(F("posts_count") + delta, 0)
        )


@receiver(post_save, sender=Post)
def _post_maintain_posts_count(sender, instance: Post, created: bool, **kwargs):
    if kwargs.get("raw"):
        return
    prev = getattr(instance, "_z_prev_root_live", False)
    now = instance.parent_id is None and not instance.is_deleted
    delta = (1 if now else 0) - (1 if prev else 0)
    if delta:
        _adjust_author_posts_count(instance.author_id, delta)


@receiver(post_delete, sender=Post)
def _post_delete_maintain_posts_count(sender, instance: Post, **kwargs):
    if instance.parent_id is None and not instance.is_deleted:
        _adjust_author_posts_count(instance.author_id, -1)


@receiver(post_save, sender=Like)
def _like_adjust_post_count(sender, instance: Like, created: bool, **kwargs):
    if kwargs.get("raw") or not created:
        return
    with transaction.atomic():
        Post.objects.filter(pk=instance.post_id).update(like_count=F("like_count") + 1)


@receiver(post_delete, sender=Like)
def _like_delete_adjust_post_count(sender, instance: Like, **kwargs):
    with transaction.atomic():
        Post.objects.filter(pk=instance.post_id).update(
            like_count=Greatest(F("like_count") - 1, 0)
        )


@receiver(post_save, sender=Repost)
def _repost_adjust_post_count(sender, instance: Repost, created: bool, **kwargs):
    if kwargs.get("raw") or not created:
        return
    with transaction.atomic():
        Post.objects.filter(pk=instance.post_id).update(repost_count=F("repost_count") + 1)


@receiver(post_delete, sender=Repost)
def _repost_delete_adjust_post_count(sender, instance: Repost, **kwargs):
    with transaction.atomic():
        Post.objects.filter(pk=instance.post_id).update(
            repost_count=Greatest(F("repost_count") - 1, 0)
        )


@receiver(post_save, sender=Follow)
def _follow_adjust_profile_counts(sender, instance: Follow, created: bool, **kwargs):
    if kwargs.get("raw") or not created:
        return
    from sites.z.models import ZProfile

    with transaction.atomic():
        ZProfile.objects.filter(user_id=instance.following_id).update(
            followers_count=F("followers_count") + 1
        )
        ZProfile.objects.filter(user_id=instance.follower_id).update(
            following_count=F("following_count") + 1
        )


@receiver(post_delete, sender=Follow)
def _follow_delete_adjust_profile_counts(sender, instance: Follow, **kwargs):
    from sites.z.models import ZProfile

    with transaction.atomic():
        ZProfile.objects.filter(user_id=instance.following_id).update(
            followers_count=Greatest(F("followers_count") - 1, 0)
        )
        ZProfile.objects.filter(user_id=instance.follower_id).update(
            following_count=Greatest(F("following_count") - 1, 0)
        )
