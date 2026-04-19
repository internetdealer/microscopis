from django.core.management.base import BaseCommand
from django.db import transaction

from sites.vestige.models import VestigeExhibit
from sites.vestige.seed_data import exhibit_rows


class Command(BaseCommand):
    help = "Load Vestige exhibits (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            VestigeExhibit.objects.all().delete()
            n = 0
            for row in exhibit_rows():
                VestigeExhibit.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Vestige: {n} exhibits loaded."))
