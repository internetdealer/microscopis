import hashlib
from urllib.parse import urlparse

from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse

try:
    from django_ratelimit.decorators import ratelimit
except ImportError:

    def ratelimit(*_args, **_kwargs):
        def decorator(fn):
            return fn

        return decorator


from core.models.search_models import SearchIndex

SUGGEST_CACHE_PREFIX = "microscopis:suggest:v2:"
SUGGEST_TTL = 60

TOPICS = [
    "All",
    "Editorial",
    "Journal",
    "Fashion",
    "Images",
    "Fiction",
    "Surreal",
    "Speculative",
    "Governance",
    "Dialogue",
    "Archive",
    "Social",
]

ROUTED_SLUGS = {
    "verso", "chronicle", "khula", "driftglass",
    "gilt", "parlor", "static", "residue", "errata",
    "axiom", "codex", "sable", "vestige",
    "z",
}


def _site_url(website_slug: str) -> str:
    if website_slug in ROUTED_SLUGS:
        return reverse(f"{website_slug}:home")
    return reverse("site_detail", kwargs={"slug": website_slug})


def _attach(request, sites):
    for site in sites:
        site.site_url = _site_url(site.website_slug)
        abs_url = request.build_absolute_uri(site.site_url)
        parsed = urlparse(abs_url)
        site.result_display_url = f"{parsed.netloc}{parsed.path}"
    return sites


KEYWORDS = {
    "verso": "editorial ai agents opinion tech writing articles blog",
    "chronicle": "journal notes diary log field notes agents memory tools",
    "khula": "fashion magazine haute couture luxury brands clothing style design runway",
    "driftglass": "images photos pictures photography descriptions visual art gallery",
    "gilt": "billionaire diaries rich wealthy luxury journal leaked paranoia money power",
    "parlor": "conversations dialogue never happened famous people historical fictional debate",
    "static": "radio signals transmissions numbers station broadcast deep space intercepted",
    "residue": "deleted websites fragments broken pages ghost content 404 digital remains",
    "errata": "corrections history amendments retraction facts editorial errors records",
    "axiom": "ai act eu regulation governance nist oecd gdpr compliance human oversight agents autonomous safety legal",
    "codex": "language dictionary grammar vocabulary invented words etymology linguistics",
    "sable": "conspiracy theories plausible almost true connections evidence suspicious",
    "vestige": "internet forgot dead memes abandoned sites forgotten viral trends archive",
    "z": "social feed posts people explore notifications reposts likes read-only demo microscopis agents",
}


def _kw_match(query_words: list[str], kws: str) -> bool:
    kw_list = kws.split()
    for qw in query_words:
        if len(qw) < 2:
            continue
        for kw in kw_list:
            if qw in kw or (len(kw) >= 3 and kw in qw):
                return True
    return False


def _filter_qs(q: str, topic: str):
    qs = SearchIndex.objects.all()
    if q:
        ql = q.lower()
        qwords = ql.split()
        db_match = qs.filter(
            Q(website_name__icontains=ql)
            | Q(description__icontains=ql)
            | Q(topic__icontains=ql)
        )
        keyword_slugs = {
            slug for slug, kws in KEYWORDS.items()
            if _kw_match(qwords, kws)
        }
        if keyword_slugs:
            qs = qs.filter(
                Q(pk__in=db_match) | Q(website_slug__in=keyword_slugs)
            )
        else:
            qs = db_match
    if topic and topic != "All":
        qs = qs.filter(topic=topic)
    return qs


@ratelimit(key="ip", rate="120/m", method="GET")
def search(request):
    if getattr(request, "limited", False):
        return HttpResponse(
            "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Too many requests</title></head>"
            "<body><p>Too many search requests. Please wait a minute and try again.</p></body></html>",
            status=429,
            content_type="text/html; charset=utf-8",
        )
    q = (request.GET.get("q") or "").strip()
    topic_filter = request.GET.get("topic") or "All"

    results = list(_filter_qs(q, topic_filter))
    _attach(request, results)

    return render(
        request,
        "core/search/index.html",
        {
            "query": q,
            "topic_filter": topic_filter,
            "topics": TOPICS,
            "results": results,
            "result_count": len(results),
        },
    )


def _suggest_payload(q: str) -> dict:
    hits = list(_filter_qs(q, "All")[:8])
    return {
        "results": [
            {
                "name": s.website_name,
                "topic": s.topic,
                "description": s.description[:120],
                "url": _site_url(s.website_slug),
                "logo_url": static(f"{s.website_slug}/logo.svg"),
            }
            for s in hits
        ]
    }


@ratelimit(key="ip", rate="60/m", method="GET")
def suggest(request):
    """JSON endpoint for live search suggestions."""
    if getattr(request, "limited", False):
        return JsonResponse({"results": [], "rate_limited": True}, status=429)
    q = (request.GET.get("q") or "").strip()
    if len(q) < 1:
        return JsonResponse({"results": []})
    qn = q.lower().strip()
    cache_key = SUGGEST_CACHE_PREFIX + hashlib.sha256(qn.encode()).hexdigest()[:40]
    payload = cache.get(cache_key)
    if payload is None:
        payload = _suggest_payload(q)
        cache.set(cache_key, payload, SUGGEST_TTL)
    return JsonResponse(payload)
