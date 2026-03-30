"""Shared template context for VERSO views."""

from __future__ import annotations

from sites.verso.models import VersoCategory


def verso_nav_context() -> dict:
    cats = list(VersoCategory.objects.order_by("sort_order", "slug"))
    first_slug = cats[0].slug if cats else "ai"
    return {
        "nav_categories": cats,
        "default_category_slug": first_slug,
    }
