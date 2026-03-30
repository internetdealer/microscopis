from django.core.management import call_command
from django.core.management.base import BaseCommand

from core.models.content_models import WebsiteContent
from core.models.search_models import SearchIndex


class Command(BaseCommand):
    help = "Seed SearchIndex with VERSO and run seed_verso (idempotent)."

    def handle(self, *args, **options):
        _, created = SearchIndex.objects.update_or_create(
            website_slug="verso",
            defaults={
                "website_name": "VERSO",
                "description": (
                    "Editorial on AI, autonomous agents, and human judgment—"
                    "models, agents, and the human work of steering both."
                ),
                "topic": "Editorial",
                "is_featured": True,
            },
        )
        removed = SearchIndex.objects.exclude(website_slug="verso").delete()[0]
        wc_removed = WebsiteContent.objects.all().delete()[0]
        self.stdout.write(
            self.style.SUCCESS(
                f"SearchIndex: verso {'created' if created else 'updated'}; "
                f"removed {removed} other row(s). WebsiteContent rows removed: {wc_removed}."
            )
        )
        call_command("seed_verso")
