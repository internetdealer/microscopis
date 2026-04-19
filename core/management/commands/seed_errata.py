from django.core.management.base import BaseCommand
from django.db import transaction

from sites.errata.models import ErrataCorrection
from sites.errata.seed_data import correction_rows


class Command(BaseCommand):
    help = "Load Errata correction data (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ErrataCorrection.objects.all().delete()
            n = 0
            for row in correction_rows():
                ErrataCorrection.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Errata: {n} entries loaded."))
