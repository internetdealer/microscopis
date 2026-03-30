from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from sites.verso import articles
from sites.verso.context import verso_nav_context
from sites.verso.models import VersoArticle, VersoCategory


def home(request):
    subscribed = request.GET.get("sub") == "1"
    ctx = verso_nav_context()
    article_list = articles.get_article_list()
    featured = articles.get_featured_articles()
    author_count = VersoArticle.objects.values("author").distinct().count()
    ctx.update(
        {
            "articles": article_list,
            "featured": featured,
            "subscribed": subscribed,
            "nav_active": "index",
            "article_count": VersoArticle.objects.count(),
            "author_count": author_count,
            "topic_count": len(ctx["nav_categories"]),
        }
    )
    return render(request, "verso/home.html", ctx)


def newsletter_subscribe(request):
    if request.method == "POST":
        return redirect(reverse("verso:home") + "?sub=1")
    return redirect("verso:home")


def about(request):
    ctx = verso_nav_context()
    ctx["nav_active"] = "about"
    return render(request, "verso/about.html", ctx)


def category_view(request, category: str):
    cat = get_object_or_404(VersoCategory, slug=category)
    ctx = verso_nav_context()
    ctx.update(
        {
            "category": cat.slug,
            "category_name": cat.name,
            "category_description": cat.description,
            "articles": articles.get_articles_by_category(cat.slug),
            "all_categories": ctx["nav_categories"],
            "nav_active": cat.slug,
        }
    )
    return render(request, "verso/category.html", ctx)


def article_detail(request, slug: str):
    article = articles.get_article_by_slug(slug)
    if not article:
        raise Http404("Article not found")
    related = [
        a
        for a in articles.get_articles_by_category(article["category"])
        if a["id"] != article["id"]
    ][:2]
    paragraphs = [p.strip() for p in article["content"].split("\n\n") if p.strip()]
    ctx = verso_nav_context()
    ctx.update(
        {
            "article": article,
            "related": related,
            "paragraphs": paragraphs,
            "nav_active": article["category"],
        }
    )
    return render(request, "verso/article.html", ctx)
