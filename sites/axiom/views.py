from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.axiom.models import AxiomLaw

LAW_TYPE_LABELS = dict(AxiomLaw.LAW_TYPES)

AXIOM_PER_PAGE = 20


def home(request):
    qs = AxiomLaw.objects.all().defer("body")
    law_type = request.GET.get("type", "")
    civilization = request.GET.get("civ", "")
    if law_type and law_type in LAW_TYPE_LABELS:
        qs = qs.filter(law_type=law_type)
    if civilization:
        qs = qs.filter(civilization_name=civilization)
    qs = qs.order_by("civilization_name", "article_number")
    paginator = Paginator(qs, AXIOM_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    laws = list(page_obj.object_list)
    instruments = list(
        AxiomLaw.objects.values_list("civilization_name", flat=True)
        .distinct()
        .order_by("civilization_name")
    )
    return render(
        request,
        "axiom/index.html",
        {
            "laws": laws,
            "instruments": instruments,
            "law_types": AxiomLaw.LAW_TYPES,
            "current_type": law_type,
            "current_civ": civilization,
            "total_count": paginator.count,
            "page_obj": page_obj,
        },
    )


def law_detail(request, slug: str):
    law = get_object_or_404(AxiomLaw, slug=slug)
    same_instrument = list(
        AxiomLaw.objects.filter(civilization_name=law.civilization_name)
        .exclude(pk=law.pk)
        .defer("body")
        .order_by("article_number")[:6]
    )
    paragraphs = [p.strip() for p in law.body.split("\n\n") if p.strip()]
    return render(
        request,
        "axiom/detail.html",
        {
            "law": law,
            "paragraphs": paragraphs,
            "same_instrument": same_instrument,
        },
    )
