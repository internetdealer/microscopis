from django.core.management.base import BaseCommand
from django.db import transaction

from sites.sable.models import SableTheory
from sites.sable.seed_data import theory_rows


class Command(BaseCommand):
    help = "Load Sable theories (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            SableTheory.objects.all().delete()
            n = 0
            for row in theory_rows():
                SableTheory.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Sable: {n} theories loaded."))
