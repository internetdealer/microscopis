from django.core.management.base import BaseCommand
from django.db import transaction

from core.utils.bulk_generators import khula_generated_articles
from core.utils.image_urls import ensure_reachable_image_url
from sites.khula.models import KhulaArticle, KhulaCategory
from sites.khula.seed_data import ARTICLES, CATEGORIES

TARGET_ARTICLES = 100


class Command(BaseCommand):
    help = "Load Khula categories and articles (replaces existing Khula rows)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-image-check",
            action="store_true",
            help="Do not HTTP-check hero URLs (faster; may keep broken links).",
        )

    def handle(self, *args, **options):
        verify = not options.get("skip_image_check")
        warn = (
            (lambda m: self.stdout.write(self.style.WARNING(m))) if verify else None
        )

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

            base = list(ARTICLES)
            extra = max(0, TARGET_ARTICLES - len(base))
            articles = base + khula_generated_articles(len(base), extra)

            n = 0
            for row in articles:
                raw_img = row.get("image_url", "")
                img = (
                    ensure_reachable_image_url(raw_img, warn)
                    if verify
                    else raw_img
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
                    image_credit=row.get("image_credit", ""),
                )
                n += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Khula: {len(cat_map)} categories, {n} articles loaded."
            )
        )
