from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.errata.models import ErrataCorrection
from sites.errata.seed_data import correction_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Errata (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ErrataCorrection.objects.all().delete()
            b = take_ingested_for_site("errata", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.errata_row(ing, i)
                    t = d["issued_at"]
                    if timezone.is_naive(t):
                        d["issued_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    ErrataCorrection.objects.create(**d)
                    n += 1
            else:
                for row in correction_rows():
                    ErrataCorrection.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Errata: {n} entries loaded."))
