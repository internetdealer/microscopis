from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from sites.khula import articles
from sites.khula.context import khula_nav_context
from sites.khula.models import KhulaArticle, KhulaCategory

KHULA_PER_PAGE = 12


def _card_from_public(a: dict) -> dict:
    """Shape for home + category list templates (matches original Khula demo keys)."""
    img = a.get("image_url") or ""
    return {
        "slug": a["id"],
        "title": a["title"],
        "category": a["category_name"],
        "date": a["date"],
        "dek": a["excerpt"],
        "image": img,
        "thumb": img,
    }


def _khula_article_base_qs():
    return KhulaArticle.objects.select_related("category").order_by(
        "-published_at", "-is_featured", "slug"
    )


def _lead_and_grid_from_page(page_num: int, raw_page_models: list) -> tuple:
    """Page 1: lead + grid from the same page slice; later pages: grid only."""
    cards = [_card_from_public(a.to_public_dict()) for a in raw_page_models]
    if page_num != 1 or not raw_page_models:
        return None, cards
    lead_idx = next(
        (i for i, a in enumerate(raw_page_models) if a.is_featured),
        0,
    )
    lead = cards[lead_idx]
    grid = [c for i, c in enumerate(cards) if i != lead_idx]
    return lead, grid


def home(request):
    ctx = khula_nav_context()
    q = request.GET.get("q", "").strip()
    base = _khula_article_base_qs()
    if q:
        low = q.lower()
        base = base.filter(
            Q(title__icontains=low)
            | Q(excerpt__icontains=low)
            | Q(body__icontains=low)
        )

    paginator = Paginator(base, KHULA_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    raw_page = list(page_obj.object_list)
    lead, grid_articles = _lead_and_grid_from_page(page_obj.number, raw_page)

    if q and not raw_page:
        ctx.update(
            {
                "lead": None,
                "grid_articles": [],
                "search_query": q,
                "nav_active": "index",
                "page_obj": page_obj,
            }
        )
        return render(request, "khula/home.html", ctx)

    ctx.update(
        {
            "lead": lead,
            "grid_articles": grid_articles,
            "search_query": q,
            "nav_active": "index",
            "page_obj": page_obj,
        }
    )
    return render(request, "khula/home.html", ctx)


def about(request):
    ctx = khula_nav_context()
    ctx["nav_active"] = "about"
    return render(request, "khula/about.html", ctx)


def contact(request):
    ctx = khula_nav_context()
    ctx["nav_active"] = "contact"
    return render(request, "khula/contact.html", ctx)


def categories_index(request):
    ctx = khula_nav_context()
    rows = []
    for c in KhulaCategory.objects.annotate(n=Count("articles")).order_by(
        "sort_order", "slug"
    ):
        rows.append(
            {
                "slug": c.slug,
                "title": c.name,
                "blurb": c.description,
                "count": c.n,
            }
        )
    ctx.update({"categories": rows, "nav_active": "categories"})
    return render(request, "khula/categories.html", ctx)


def category_view(request, category: str):
    cat = get_object_or_404(KhulaCategory, slug=category)
    ctx = khula_nav_context()
    qs = _khula_article_base_qs().filter(category=cat)
    paginator = Paginator(qs, KHULA_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    article_rows = [
        _card_from_public(a.to_public_dict()) for a in page_obj.object_list
    ]
    ctx.update(
        {
            "category": {
                "title": cat.name,
                "blurb": cat.description,
            },
            "articles": article_rows,
            "nav_active": cat.slug,
            "page_obj": page_obj,
        }
    )
    return render(request, "khula/category.html", ctx)


def article_detail(request, slug: str):
    article = articles.get_article_by_slug(slug)
    if not article:
        raise Http404("Article not found")
    paragraphs = [p.strip() for p in article["content"].split("\n\n") if p.strip()]
    display = {
        "title": article["title"],
        "category": article["category_name"],
        "date": article["date"],
        "dek": article["excerpt"],
        "image": article.get("image_url") or "",
        "paragraphs": paragraphs,
    }
    ctx = khula_nav_context()
    ctx.update(
        {
            "article": display,
            "nav_active": article["category"],
        }
    )
    return render(request, "khula/article.html", ctx)
