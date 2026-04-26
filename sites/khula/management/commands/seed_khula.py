import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.ingest import mapping as ingest_mapping
from core.utils.bulk_generators import khula_generated_articles
from core.utils.sourced_media import download_hero_to_media
from core.utils.synthetic_media import ensure_khula_excerpt_honesty, generate_khula_hero
from core.utils.web_seed import take_ingested_for_site
from sites.khula.models import KhulaArticle, KhulaCategory
from sites.khula.seed_data import ARTICLES, CATEGORIES

TARGET_ARTICLES = 100


class Command(BaseCommand):
    help = "Load Khula categories and articles (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            KhulaArticle.objects.all().delete()
            KhulaCategory.objects.all().delete()

            cat_map: dict[str, KhulaCategory] = {}
            for c in CATEGORIES:
                cat_map[c["slug"]] = KhulaCategory.objects.create(
                    slug=c["slug"],
                    name=c["name"],
                    description=c["description"],
                    sort_order=c["sort_order"],
                )
            cat_slugs = [c["slug"] for c in CATEGORIES]
            b = take_ingested_for_site("khula", n=TARGET_ARTICLES)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    cs = cat_slugs[i % len(cat_slugs)]
                    rm = min(22, max(3, len(ing.body) // 3500))
                    d = ingest_mapping.khula_rows(
                        ing,
                        category_slug=cs,
                        read_minutes=rm,
                        is_featured=(i % 11 == 0),
                    )
                    cslug = d.pop("_category_slug")
                    KhulaArticle.objects.create(
                        slug=d["slug"],
                        title=d["title"],
                        excerpt=d["excerpt"],
                        body=d["body"],
                        author=d["author"],
                        published_at=d["published_at"],
                        read_minutes=d["read_minutes"],
                        is_featured=d["is_featured"],
                        category=cat_map[cslug],
                        image_url=d["image_url"],
                        image_credit=d["image_credit"],
                    )
                    n += 1
            else:
                base = list(ARTICLES)
                extra = max(0, TARGET_ARTICLES - len(base))
                articles = base + khula_generated_articles(len(base), extra)
                ensure_khula_excerpt_honesty(articles)
                for row in articles:
                    src_url = (row.get("sourced_image_url") or "").strip()
                    src_credit = (row.get("sourced_image_credit") or "").strip()
                    if src_url and not src_credit:
                        raise CommandError(
                            f'slug {row.get("slug")!r}: sourced_image_url requires sourced_image_credit'
                        )
                    if src_url and src_credit:
                        try:
                            img, _n = download_hero_to_media(
                                src_url, site="khula", filename_stem=row["slug"]
                            )
                        except (OSError, ValueError, requests.RequestException) as e:
                            raise CommandError(
                                f'slug {row.get("slug")!r}: could not download sourced image: {e}'
                            ) from e
                        cred = src_credit
                    else:
                        explicit = (row.get("image_url") or "").strip()
                        if explicit:
                            img = explicit
                            cred = (row.get("image_credit") or "").strip() or "Image"
                        else:
                            img, cred = generate_khula_hero(
                                row["slug"],
                                category=row["category"],
                                title=row.get("title", ""),
                                excerpt=row.get("excerpt", ""),
                            )
                    KhulaArticle.objects.create(
                        slug=row["slug"],
                        title=row["title"],
                        excerpt=row["excerpt"],
                        body=row["body"],
                        author=row["author"],
                        published_at=row["published_at"],
                        read_minutes=row["read_minutes"],
                        is_featured=row["is_featured"],
                        category=cat_map[row["category"]],
                        image_url=img,
                        image_credit=cred,
                    )
                    n += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Khula: {len(cat_map)} categories, {n} articles loaded."
            )
        )
