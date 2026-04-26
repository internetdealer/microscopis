from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.parlor.models import ParlorDialogue
from sites.parlor.seed_data import parlor_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Parlor dialogues (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ParlorDialogue.objects.all().delete()
            b = take_ingested_for_site("parlor", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.parlor_row(ing, i)
                    t = d["created_at"]
                    if timezone.is_naive(t):
                        d["created_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    ParlorDialogue.objects.create(**d)
                    n += 1
            else:
                for row in parlor_rows():
                    ParlorDialogue.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Parlor: {n} dialogues loaded."))
