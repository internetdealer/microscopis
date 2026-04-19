"""Template helpers for classic ?page= pagination."""

from __future__ import annotations

from django import template

register = template.Library()


@register.simple_tag
def pagination_href(request, page_num: int) -> str:
    """Build query string with all current GET params and ``page`` set to ``page_num``."""
    q = request.GET.copy()
    q["page"] = str(page_num)
    return "?" + q.urlencode()
