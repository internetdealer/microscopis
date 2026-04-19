from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.residue.models import ResidueFragment

RESIDUE_PER_PAGE = 16


def home(request):
    """Bento wall: one irregular grid of fragments (broken-layout metaphor)."""
    qs = ResidueFragment.objects.order_by("-archived_at")
    paginator = Paginator(qs, RESIDUE_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    fragments = list(page_obj.object_list)
    return render(
        request,
        "residue/index.html",
        {
            "fragments": fragments,
            "total_count": paginator.count,
            "page_obj": page_obj,
        },
    )


def entry_detail(request, slug: str):
    entry = get_object_or_404(ResidueFragment, slug=slug)
    others = list(
        ResidueFragment.objects.exclude(pk=entry.pk).order_by("-archived_at")[:4]
    )
    paragraphs = [p.strip() for p in entry.recovered_text.split("\n\n") if p.strip()]
    return render(
        request,
        "residue/detail.html",
        {"entry": entry, "paragraphs": paragraphs, "others": others},
    )
