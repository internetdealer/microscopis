from django.core.cache import cache
from django.core.management import call_command
from django.core.management.base import BaseCommand

from core.models.content_models import WebsiteContent
from core.models.search_models import SearchIndex

# Driftglass runs last so the DB reflects the full image registry after other seeds are defined in code.
ALL_SLUGS = [
    "verso",
    "chronicle",
    "khula",
    "gilt",
    "parlor",
    "static",
    "residue",
    "errata",
    "axiom",
    "codex",
    "sable",
    "vestige",
    "z",
    "driftglass",
]

SITES = [
    ("verso", "VERSO", "Editorial on AI, autonomous agents, and human judgment.", "Editorial"),
    ("chronicle", "Chronicle", "Read-only AI-authored journal: field notes on agents, tools, and memory.", "Journal"),
    ("khula", "Khula", "Niche high-fashion magazine: maisons, avant-garde, and machine-authored essays.", "Fashion"),
    ("driftglass", "Driftglass", "Agents fetch remote images and file long-form descriptions—telemetry dressed as criticism.", "Images"),
    ("gilt", "Gilt", "Leaked private journal entries from fictional ultra-rich people—paranoia, absurd luxury, power plays.", "Fiction"),
    ("parlor", "Parlor", "Dialogue between people who never met—Elon Musk vs da Vinci, Napoleon vs Steve Jobs.", "Dialogue"),
    ("static", "Static", "Transcriptions of mysterious radio signals from nowhere—numbers stations, alien broadcasts, deep space noise.", "Fiction"),
    ("residue", "Residue", "Fragments of deleted websites—broken pages, ghost content, 404 archaeology.", "Archive"),
    ("errata", "Errata", "Official-sounding corrections and amendments to historical facts, as if history had editors.", "Speculative"),
    ("axiom", "Axiom", "Agent governance: paraphrased readings of real AI laws and standards (EU AI Act, NIST, OECD, GDPR…) that keep autonomy subordinate to humans.", "Governance"),
    ("codex", "Codex", "Dictionaries and grammar guides for languages that don't exist—vocabulary, etymology, sample poetry.", "Surreal"),
    ("sable", "Sable", "Conspiracy theories that are almost plausible—real events connected with fictional dots.", "Fiction"),
    ("vestige", "Vestige", "A museum of things the internet forgot—dead memes explained, abandoned projects documented.", "Archive"),
    ("z", "Z", "Synthetic social surface: staged posts and graph edges for future autonomous operators—observe only.", "Social"),
]


class Command(BaseCommand):
    help = "Seed SearchIndex for all sites, clear legacy content, run all site seeds."

    def handle(self, *args, **options):
        cache.clear()
        SearchIndex.objects.exclude(website_slug__in=ALL_SLUGS).delete()

        for slug, name, desc, topic in SITES:
            SearchIndex.objects.update_or_create(
                website_slug=slug,
                defaults={
                    "website_name": name,
                    "description": desc,
                    "topic": topic,
                    "is_featured": True,
                },
            )

        wc_removed = WebsiteContent.objects.all().delete()[0]
        count = SearchIndex.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"SearchIndex: {count} sites registered. "
                f"WebsiteContent rows removed: {wc_removed}."
            )
        )

        for slug in ALL_SLUGS:
            call_command(f"seed_{slug}")
