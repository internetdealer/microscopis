from urllib.parse import quote

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.static.models import StaticSignal

STATIC_PER_PAGE = 16


def _archive_embed_src(entry: StaticSignal) -> str:
    item_id = (entry.archive_embed_id or "").strip()
    if not item_id:
        return ""
    base = f"https://archive.org/embed/{quote(item_id, safe='')}"
    fn = (entry.archive_embed_file or "").strip()
    if fn:
        return f"{base}/{quote(fn, safe='/')}"
    return base


def home(request):
    """Signal log: tabular intercept register (not card grids)."""
    qs = StaticSignal.objects.order_by("-intercepted_at")
    paginator = Paginator(qs, STATIC_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    signals = list(page_obj.object_list)
    return render(
        request,
        "static/index.html",
        {
            "signals": signals,
            "total_count": paginator.count,
            "page_obj": page_obj,
        },
    )


def entry_detail(request, slug: str):
    entry = get_object_or_404(StaticSignal, slug=slug)
    others = list(
        StaticSignal.objects.exclude(pk=entry.pk).order_by("-intercepted_at")[:4]
    )
    paragraphs = [p.strip() for p in entry.transcript.split("\n\n") if p.strip()]
    return render(
        request,
        "static/detail.html",
        {
            "entry": entry,
            "paragraphs": paragraphs,
            "others": others,
            "archive_embed_src": _archive_embed_src(entry),
        },
    )
