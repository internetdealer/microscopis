from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.parlor.models import ParlorDialogue

PARLOR_PER_PAGE = 18


def home(request):
    """Playbill-style index: one continuous program of scenes (no duplicate featured grid)."""
    qs = ParlorDialogue.objects.order_by("-created_at")
    paginator = Paginator(qs, PARLOR_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    dialogues = list(page_obj.object_list)
    scene_offset = (page_obj.number - 1) * PARLOR_PER_PAGE
    return render(
        request,
        "parlor/index.html",
        {
            "dialogues": dialogues,
            "page_obj": page_obj,
            "scene_offset": scene_offset,
        },
    )


def dialogue_detail(request, slug: str):
    dialogue = get_object_or_404(ParlorDialogue, slug=slug)
    others = list(
        ParlorDialogue.objects.exclude(pk=dialogue.pk).order_by("-created_at")[:4]
    )
    turns = [p.strip() for p in dialogue.body.split("\n\n") if p.strip()]
    return render(
        request,
        "parlor/detail.html",
        {"dialogue": dialogue, "turns": turns, "others": others},
    )
