from django.shortcuts import render

from core.models.search_models import SearchIndex


def home(request):
    featured = SearchIndex.objects.filter(is_featured=True)[:10]
    return render(
        request,
        "core/main/index.html",
        {
            "featured_sites": featured,
            "site_count": SearchIndex.objects.count(),
            "topic_count": SearchIndex.objects.values("topic").distinct().count(),
            "try_terms": ["editorial", "journal", "agents", "AI"],
        },
    )
