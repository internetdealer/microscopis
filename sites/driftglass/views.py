from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from sites.driftglass.models import DriftglassImage


def home(request):
    agent = request.GET.get("agent", "").strip()

    base = DriftglassImage.objects.order_by("-created_at")
    if agent:
        base = base.filter(probe_agent=agent)

    paginator = Paginator(base, 48)
    page_obj = paginator.get_page(request.GET.get("page"))

    agents = list(
        DriftglassImage.objects.values_list("probe_agent", flat=True)
        .distinct()
        .order_by("probe_agent")
    )

    # One filtered count (same queryset as the grid), not a second global query.
    total_count = paginator.count

    return render(
        request,
        "driftglass/index.html",
        {
            "page_obj": page_obj,
            "agents": agents,
            "current_agent": agent,
            "total_count": total_count,
        },
    )


def probe_detail(request, slug: str):
    probe = get_object_or_404(DriftglassImage, slug=slug)
    others = list(
        DriftglassImage.objects.exclude(pk=probe.pk).order_by("-created_at")[:4]
    )
    paragraphs = [p.strip() for p in probe.description.split("\n\n") if p.strip()]
    return render(
        request,
        "driftglass/probe.html",
        {
            "probe": probe,
            "paragraphs": paragraphs,
            "others": others,
        },
    )


def telemetry(request):
    """Static manifesto page."""
    return render(request, "driftglass/telemetry.html")
