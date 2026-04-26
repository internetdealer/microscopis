from django.core.management.base import BaseCommand
from django.db import transaction

from core.ingest import mapping as ingest_mapping
from sites.gilt.models import GiltEntry
from sites.gilt.seed_data import entry_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Gilt diary entries (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            GiltEntry.objects.all().delete()
            b = take_ingested_for_site("gilt", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    GiltEntry.objects.create(**ingest_mapping.gilt_row(ing, i))
                    n += 1
            else:
                for row in entry_rows():
                    GiltEntry.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Gilt: {n} entries loaded."))
