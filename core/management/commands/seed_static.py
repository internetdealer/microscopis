from django.core.management.base import BaseCommand
from django.db import transaction

from sites.static.models import StaticSignal
from sites.static.seed_data import signal_rows


class Command(BaseCommand):
    help = "Load Static signal data (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            StaticSignal.objects.all().delete()
            n = 0
            for row in signal_rows():
                StaticSignal.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Static: {n} entries loaded."))
