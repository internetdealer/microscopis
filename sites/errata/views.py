from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.errata.models import ErrataCorrection

ERRATA_ARCHIVE_PER_PAGE = 12


def home(request):
    severity = request.GET.get("severity")
    qs = ErrataCorrection.objects.all().order_by("-issued_at")
    if severity in ("minor", "major", "critical", "retraction"):
        qs = qs.filter(severity=severity)

    total_count = qs.count()

    featured = list(qs.filter(is_featured=True).order_by("-issued_at")[:3])
    if not featured:
        first = qs.first()
        featured = [first] if first else []

    feat_ids = [c.pk for c in featured]
    rest_qs = qs.exclude(pk__in=feat_ids) if feat_ids else qs

    paginator = Paginator(rest_qs, ERRATA_ARCHIVE_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    entries = list(page_obj.object_list)

    return render(
        request,
        "errata/index.html",
        {
            "featured": featured,
            "entries": entries,
            "total_count": total_count,
            "page_obj": page_obj,
            "current_severity": severity,
        },
    )


def timeline(request):
    corrections = list(
        ErrataCorrection.objects.filter(fact_year__isnull=False).order_by(
            "fact_year", "-issued_at"
        )
    )
    return render(
        request,
        "errata/timeline.html",
        {"corrections": corrections},
    )


def entry_detail(request, slug: str):
    entry = get_object_or_404(ErrataCorrection, slug=slug)
    others = list(
        ErrataCorrection.objects.exclude(pk=entry.pk).order_by("-issued_at")[:4]
    )
    paragraphs = [p.strip() for p in entry.correction.split("\n\n") if p.strip()]
    return render(
        request,
        "errata/detail.html",
        {
            "entry": entry,
            "paragraphs": paragraphs,
            "others": others,
        },
    )
