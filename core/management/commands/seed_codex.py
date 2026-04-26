from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.codex.models import CodexEntry
from sites.codex.seed_data import entry_rows as codex_entry_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Codex (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            CodexEntry.objects.all().delete()
            b = take_ingested_for_site("codex", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.codex_row(ing, i)
                    t = d["created_at"]
                    if timezone.is_naive(t):
                        d["created_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    CodexEntry.objects.create(**d)
                    n += 1
            else:
                for row in codex_entry_rows():
                    CodexEntry.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Codex: {n} entries loaded."))
