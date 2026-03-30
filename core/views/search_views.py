from urllib.parse import urlparse

from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse

from core.models.search_models import SearchIndex

TOPICS = [
    "All",
    "Editorial",
]


def _site_absolute_url(request, website_slug: str) -> str:
    if website_slug == "verso":
        path = reverse("verso:home")
    else:
        path = reverse("site_detail", kwargs={"slug": website_slug})
    return request.build_absolute_uri(path)


def search(request):
    q = (request.GET.get("q") or "").strip()
    topic_filter = request.GET.get("topic") or "All"

    qs = SearchIndex.objects.all()
    if q:
        ql = q.lower()
        qs = qs.filter(
            Q(website_name__icontains=ql)
            | Q(description__icontains=ql)
            | Q(topic__icontains=ql)
        )
    if topic_filter != "All":
        qs = qs.filter(topic=topic_filter)

    results = list(qs)
    for site in results:
        abs_url = _site_absolute_url(request, site.website_slug)
        site.result_absolute_url = abs_url
        parsed = urlparse(abs_url)
        site.result_display_url = f"{parsed.netloc}{parsed.path}"

    return render(
        request,
        "core/search/index.html",
        {
            "query": q,
            "topic_filter": topic_filter,
            "topics": TOPICS,
            "results": results,
            "result_count": len(results),
        },
    )
