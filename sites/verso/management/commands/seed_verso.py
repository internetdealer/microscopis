from django.core.management.base import BaseCommand
from django.db import transaction

from core.utils.bulk_generators import verso_generated_articles
from core.utils.image_urls import ensure_reachable_image_url
from sites.verso.models import VersoArticle, VersoCategory
from sites.verso.seed_data import ARTICLES, CATEGORIES

TARGET_ARTICLES = 100


class Command(BaseCommand):
    help = "Load VERSO categories and articles into the database (replaces existing VERSO rows)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--verify-images",
            action="store_true",
            help="HTTP-check each hero image URL and substitute a fallback if unreachable (slower).",
        )

    def handle(self, *args, **options):
        verify = options.get("verify_images")
        warn = (
            (lambda m: self.stdout.write(self.style.WARNING(m))) if verify else None
        )

        with transaction.atomic():
            VersoArticle.objects.all().delete()
            VersoCategory.objects.all().delete()

            cat_map: dict[str, VersoCategory] = {}
            for c in CATEGORIES:
                cat_map[c["slug"]] = VersoCategory.objects.create(
                    slug=c["slug"],
                    name=c["name"],
                    description=c["description"],
                    sort_order=c["sort_order"],
                )

            base = list(ARTICLES)
            extra = max(0, TARGET_ARTICLES - len(base))
            articles = base + verso_generated_articles(len(base), extra)

            n = 0
            for row in articles:
                raw_img = row.get("image_url", "")
                img = (
                    ensure_reachable_image_url(raw_img, warn)
                    if verify
                    else raw_img
                )
                VersoArticle.objects.create(
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
                f"VERSO: {len(cat_map)} categories, {n} articles loaded."
            )
        )
