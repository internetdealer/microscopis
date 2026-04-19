from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.codex.models import CodexEntry

CODEX_PER_PAGE = 24


def home(request):
    qs = CodexEntry.objects.all().defer("etymology")
    letter = request.GET.get("letter", "").upper()
    entry_type = request.GET.get("type", "")
    if letter and len(letter) == 1 and letter.isalpha():
        qs = qs.filter(letter=letter)
    if entry_type and entry_type in dict(CodexEntry.ENTRY_TYPES):
        qs = qs.filter(entry_type=entry_type)
    qs = qs.order_by("term")
    paginator = Paginator(qs, CODEX_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    entries = list(page_obj.object_list)
    letters_used = sorted(
        CodexEntry.objects.values_list("letter", flat=True).distinct()
    )
    return render(
        request,
        "codex/index.html",
        {
            "entries": entries,
            "letters": letters_used,
            "entry_types": CodexEntry.ENTRY_TYPES,
            "current_letter": letter,
            "current_type": entry_type,
            "total_count": paginator.count,
            "page_obj": page_obj,
        },
    )


def entry_detail(request, slug: str):
    entry = get_object_or_404(CodexEntry, slug=slug)
    same_type = list(
        CodexEntry.objects.filter(entry_type=entry.entry_type)
        .exclude(pk=entry.pk)
        .defer("definition", "etymology")
        .order_by("term")[:6]
    )
    paragraphs = [p.strip() for p in entry.definition.split("\n\n") if p.strip()]
    return render(
        request,
        "codex/detail.html",
        {"entry": entry, "paragraphs": paragraphs, "same_type": same_type},
    )
