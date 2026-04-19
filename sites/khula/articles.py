"""Read-only accessors for Khula views. Content lives in ``khula.KhulaArticle``."""

from __future__ import annotations

from sites.khula.models import KhulaArticle


def get_article_list() -> list[dict]:
    qs = KhulaArticle.objects.select_related("category").order_by("-published_at")
    return [a.to_public_dict() for a in qs]


def get_article_by_slug(slug: str) -> dict | None:
    a = KhulaArticle.objects.select_related("category").filter(slug=slug).first()
    return a.to_public_dict() if a else None


def get_articles_by_category(category_slug: str) -> list[dict]:
    qs = (
        KhulaArticle.objects.select_related("category")
        .filter(category__slug=category_slug)
        .order_by("-published_at")
    )
    return [a.to_public_dict() for a in qs]


def get_featured_articles() -> list[dict]:
    qs = (
        KhulaArticle.objects.select_related("category")
        .filter(is_featured=True)
        .order_by("-published_at")
    )
    return [a.to_public_dict() for a in qs]
