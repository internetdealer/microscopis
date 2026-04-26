from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.static.models import StaticSignal
from sites.static.seed_data import signal_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Static signal data (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            StaticSignal.objects.all().delete()
            b = take_ingested_for_site("static", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.static_row(ing, i)
                    t = d["intercepted_at"]
                    if timezone.is_naive(t):
                        d["intercepted_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    StaticSignal.objects.create(**d)
                    n += 1
            else:
                for row in signal_rows():
                    StaticSignal.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Static: {n} entries loaded."))
