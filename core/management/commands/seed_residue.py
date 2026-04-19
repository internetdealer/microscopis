from django.core.management.base import BaseCommand
from django.db import transaction

from sites.residue.models import ResidueFragment
from sites.residue.seed_data import fragment_rows


class Command(BaseCommand):
    help = "Load Residue fragment data (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ResidueFragment.objects.all().delete()
            n = 0
            for row in fragment_rows():
                ResidueFragment.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Residue: {n} entries loaded."))
