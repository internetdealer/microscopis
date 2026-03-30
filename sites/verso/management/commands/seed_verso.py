from django.core.management.base import BaseCommand
from django.db import transaction

from sites.verso.models import VersoArticle, VersoCategory
from sites.verso.seed_data import ARTICLES, CATEGORIES


class Command(BaseCommand):
    help = "Load VERSO categories and articles into the database (replaces existing VERSO rows)."

    def handle(self, *args, **options):
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

            n = 0
            for row in ARTICLES:
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
                    image_url=row.get("image_url", ""),
                    image_credit=row.get("image_credit", ""),
                )
                n += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"VERSO: {len(cat_map)} categories, {n} articles loaded."
            )
        )
