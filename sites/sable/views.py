from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.sable.models import SableTheory

PLAUSIBILITY_CHOICES = [c[0] for c in SableTheory.PLAUSIBILITY]

SABLE_ARCHIVE_PER_PAGE = 12


def home(request):
    current_plausibility = request.GET.get("plausibility", "")
    if current_plausibility and current_plausibility not in PLAUSIBILITY_CHOICES:
        current_plausibility = ""

    qs = SableTheory.objects.all().defer("evidence_cited", "wikipedia_urls").order_by(
        "-published_at"
    )
    if current_plausibility:
        qs = qs.filter(plausibility=current_plausibility)

    featured = list(qs.filter(is_featured=True).order_by("-published_at")[:3])
    if not featured:
        first = qs.first()
        featured = [first] if first else []

    feat_ids = [t.pk for t in featured]
    rest_qs = qs.exclude(pk__in=feat_ids) if feat_ids else qs

    paginator = Paginator(rest_qs, SABLE_ARCHIVE_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    theories = list(page_obj.object_list)

    return render(
        request,
        "sable/index.html",
        {
            "featured": featured,
            "theories": theories,
            "plausibilities": SableTheory.PLAUSIBILITY,
            "current_plausibility": current_plausibility,
            "page_obj": page_obj,
        },
    )


def theory_detail(request, slug: str):
    theory = get_object_or_404(SableTheory, slug=slug)
    others = list(
        SableTheory.objects.exclude(pk=theory.pk).order_by("-published_at")[:4]
    )
    paragraphs = [p.strip() for p in theory.body.split("\n\n") if p.strip()]
    return render(
        request,
        "sable/detail.html",
        {
            "theory": theory,
            "paragraphs": paragraphs,
            "others": others,
        },
    )
