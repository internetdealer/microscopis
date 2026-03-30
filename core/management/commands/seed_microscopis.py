from django.core.management import call_command
from django.core.management.base import BaseCommand

from core.models.content_models import WebsiteContent
from core.models.search_models import SearchIndex


class Command(BaseCommand):
    help = "Seed SearchIndex (VERSO + Chronicle), clear legacy content, run site seeds."

    def handle(self, *args, **options):
        SearchIndex.objects.exclude(website_slug__in=["verso", "chronicle"]).delete()

        _, v_created = SearchIndex.objects.update_or_create(
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
        _, c_created = SearchIndex.objects.update_or_create(
            website_slug="chronicle",
            defaults={
                "website_name": "Chronicle",
                "description": (
                    "Read-only AI-authored journal: field notes on agents, tools, memory, "
                    "and human-in-the-loop operations."
                ),
                "topic": "Journal",
                "is_featured": True,
            },
        )

        wc_removed = WebsiteContent.objects.all().delete()[0]
        self.stdout.write(
            self.style.SUCCESS(
                f"SearchIndex: verso {'created' if v_created else 'updated'}, "
                f"chronicle {'created' if c_created else 'updated'}. "
                f"WebsiteContent rows removed: {wc_removed}."
            )
        )
        call_command("seed_verso")
        call_command("seed_chronicle")
