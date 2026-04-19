from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.vestige.models import VestigeExhibit

VESTIGE_PER_PAGE = 18


def home(request):
    qs = VestigeExhibit.objects.all().order_by("-curated_at")
    exhibit_type = request.GET.get("type", "")
    if exhibit_type and exhibit_type in dict(VestigeExhibit.EXHIBIT_TYPES):
        qs = qs.filter(exhibit_type=exhibit_type)

    total_count = qs.count()

    featured = list(qs.filter(is_featured=True).order_by("-curated_at")[:3])
    if not featured:
        first = qs.first()
        featured = [first] if first else []

    feat_ids = [e.pk for e in featured]
    rest_qs = qs.exclude(pk__in=feat_ids) if feat_ids else qs

    paginator = Paginator(rest_qs, VESTIGE_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    exhibits = list(page_obj.object_list)

    return render(
        request,
        "vestige/index.html",
        {
            "featured": featured,
            "exhibits": exhibits,
            "exhibit_types": VestigeExhibit.EXHIBIT_TYPES,
            "current_type": exhibit_type,
            "total_count": total_count,
            "page_obj": page_obj,
        },
    )


def exhibit_detail(request, slug: str):
    exhibit = get_object_or_404(VestigeExhibit, slug=slug)
    others = list(
        VestigeExhibit.objects.exclude(pk=exhibit.pk).order_by("-curated_at")[:4]
    )
    paragraphs = [p.strip() for p in exhibit.body.split("\n\n") if p.strip()]
    return render(
        request,
        "vestige/detail.html",
        {
            "exhibit": exhibit,
            "paragraphs": paragraphs,
            "others": others,
        },
    )
