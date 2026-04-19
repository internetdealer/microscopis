from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse

from core.models.search_models import SearchIndex

CACHE_KEY_HOME_SEARCHINDEX = "microscopis:home:searchindex"
HOME_SEARCHINDEX_TTL = 120

ROUTED_SLUGS = {
    "verso", "chronicle", "khula", "driftglass",
    "gilt", "parlor", "static", "residue", "errata",
    "axiom", "codex", "sable", "vestige",
    "z",
}


def _attach_urls(sites):
    for site in sites:
        if site.website_slug in ROUTED_SLUGS:
            site.site_url = reverse(f"{site.website_slug}:home")
        else:
            site.site_url = reverse("site_detail", kwargs={"slug": site.website_slug})
    return sites


def home(request):
    cached = cache.get(CACHE_KEY_HOME_SEARCHINDEX)
    if cached is None:
        # Include all featured sites (e.g. "Z" sorts last by name; avoid truncating the grid).
        featured = list(SearchIndex.objects.filter(is_featured=True)[:48])
        site_count = SearchIndex.objects.count()
        topic_count = SearchIndex.objects.values("topic").distinct().count()
        cache.set(
            CACHE_KEY_HOME_SEARCHINDEX,
            {"featured": featured, "site_count": site_count, "topic_count": topic_count},
            HOME_SEARCHINDEX_TTL,
        )
    else:
        featured = cached["featured"]
        site_count = cached["site_count"]
        topic_count = cached["topic_count"]
    _attach_urls(featured)
    return render(
        request,
        "core/main/index.html",
        {
            "featured_sites": featured,
            "site_count": site_count,
            "topic_count": topic_count,
            "try_terms": ["governance", "fiction", "archive", "eu ai", "language"],
        },
    )
