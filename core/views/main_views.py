from django.shortcuts import render

from core.models.search_models import SearchIndex


def home(request):
    featured = SearchIndex.objects.filter(is_featured=True)[:10]
    return render(
        request,
        "core/main/index.html",
        {
            "featured_sites": featured,
            "try_terms": ["editorial", "culture", "technology", "politics"],
        },
    )
