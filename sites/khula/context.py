"""Shared template context for Khula views."""

from __future__ import annotations

from sites.khula.models import KhulaCategory


def khula_nav_context() -> dict:
    cats = list(KhulaCategory.objects.order_by("sort_order", "slug"))
    first_slug = cats[0].slug if cats else "maisons"
    return {
        "nav_categories": cats,
        "default_category_slug": first_slug,
    }
