from django.core.management.base import BaseCommand
from django.db import transaction

from sites.gilt.models import GiltEntry
from sites.gilt.seed_data import entry_rows


class Command(BaseCommand):
    help = "Load Gilt diary entries (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            GiltEntry.objects.all().delete()
            n = 0
            for row in entry_rows():
                GiltEntry.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Gilt: {n} entries loaded."))
