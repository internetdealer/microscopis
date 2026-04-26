from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.sable.models import SableTheory
from sites.sable.seed_data import theory_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Sable (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            SableTheory.objects.all().delete()
            b = take_ingested_for_site("sable", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.sable_row(ing, i)
                    t = d["published_at"]
                    if timezone.is_naive(t):
                        d["published_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    SableTheory.objects.create(**d)
                    n += 1
            else:
                for row in theory_rows():
                    SableTheory.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Sable: {n} entries loaded."))
