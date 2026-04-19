from django.core.management.base import BaseCommand
from django.db import transaction

from sites.parlor.models import ParlorDialogue
from sites.parlor.seed_data import parlor_rows


class Command(BaseCommand):
    help = "Load Parlor dialogues (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ParlorDialogue.objects.all().delete()
            n = 0
            for row in parlor_rows():
                ParlorDialogue.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Parlor: {n} dialogues loaded."))
