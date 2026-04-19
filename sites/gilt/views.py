from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.gilt.models import GiltEntry

GILT_PER_PAGE = 24


def home(request):
    """Ledger-style index: single chronological table (not featured cards + grid)."""
    qs = GiltEntry.objects.order_by("-entry_date")
    paginator = Paginator(qs, GILT_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    ledger_entries = list(page_obj.object_list)
    return render(
        request,
        "gilt/index.html",
        {
            "ledger_entries": ledger_entries,
            "total_count": paginator.count,
            "page_obj": page_obj,
        },
    )


def entry_detail(request, slug: str):
    entry = get_object_or_404(GiltEntry, slug=slug)
    others = list(
        GiltEntry.objects.exclude(pk=entry.pk).order_by("-entry_date")[:4]
    )
    paragraphs = [p.strip() for p in entry.body.split("\n\n") if p.strip()]
    return render(
        request,
        "gilt/detail.html",
        {
            "entry": entry,
            "paragraphs": paragraphs,
            "others": others,
        },
    )
