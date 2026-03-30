"""
Central dispatcher for /sites/<slug>/ plus DB-backed fallback for slugs
without a custom package in sites/registry.py.
"""

from django.http import Http404
from django.shortcuts import render

from core.models.content_models import WebsiteContent
from core.models.search_models import SearchIndex

from sites.registry import SITE_VIEWS
from sites.utils import import_callable

DEFAULT_PARAGRAPHS = [
    "Welcome to this AI-generated website. This content was created entirely by artificial intelligence.",
    "The future of web content is here. AI can generate informative, engaging, and helpful content across any topic.",
    "Explore more AI-generated websites on microscopis.com, where you can discover a new dimension of the web.",
    "This is just the beginning of what's possible with AI-generated content.",
]


def site_router(request, slug: str):
    path = SITE_VIEWS.get(slug)
    if path:
        view = import_callable(path)
        return view(request)
    return site_fallback(request, slug)


def site_fallback(request, slug: str):
    """Render from SearchIndex + WebsiteContent when no sites/<package> handles this slug."""
    try:
        site = SearchIndex.objects.get(website_slug=slug)
    except SearchIndex.DoesNotExist:
        raise Http404("Site not found")

    blocks = WebsiteContent.objects.filter(site_slug=slug, page_slug="home").order_by("id")
    paragraphs = [b.content.strip() for b in blocks if b.content.strip()]
    if not paragraphs:
        paragraphs = list(DEFAULT_PARAGRAPHS)

    return render(
        request,
        "core/site_fallback.html",
        {
            "site": site,
            "paragraphs": paragraphs,
        },
    )
