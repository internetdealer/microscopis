from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.vestige.models import VestigeExhibit
from sites.vestige.seed_data import exhibit_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Vestige (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            VestigeExhibit.objects.all().delete()
            b = take_ingested_for_site("vestige", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.vestige_row(ing, i)
                    t = d["curated_at"]
                    if timezone.is_naive(t):
                        d["curated_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    VestigeExhibit.objects.create(**d)
                    n += 1
            else:
                for row in exhibit_rows():
                    VestigeExhibit.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Vestige: {n} entries loaded."))
