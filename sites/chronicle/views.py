from django.http import Http404
from django.shortcuts import get_object_or_404, render

from sites.chronicle.models import ChronicleEntry, ChronicleTag


def _sidebar_context():
    return {
        "entry_count": ChronicleEntry.objects.count(),
        "tag_list": ChronicleTag.objects.order_by("name")[:20],
    }


def index(request):
    entries = ChronicleEntry.objects.prefetch_related("tags").order_by("-published_at")
    ctx = {"entries": entries}
    ctx.update(_sidebar_context())
    return render(request, "chronicle/index.html", ctx)


def entry_detail(request, slug: str):
    entry = get_object_or_404(ChronicleEntry.objects.prefetch_related("tags"), slug=slug)
    ctx = {
        "entry": entry,
        "paragraphs": [p.strip() for p in entry.body.split("\n\n") if p.strip()],
    }
    ctx.update(_sidebar_context())
    return render(request, "chronicle/entry.html", ctx)


def tags_list(request):
    tags = ChronicleTag.objects.order_by("name")
    ctx = {"tags": tags}
    ctx.update(_sidebar_context())
    return render(request, "chronicle/tags.html", ctx)


def tag_detail(request, tag_slug: str):
    tag = get_object_or_404(ChronicleTag, slug=tag_slug)
    entries = (
        ChronicleEntry.objects.prefetch_related("tags")
        .filter(tags=tag)
        .order_by("-published_at")
    )
    ctx = {"tag": tag, "entries": entries}
    ctx.update(_sidebar_context())
    return render(request, "chronicle/tag.html", ctx)
