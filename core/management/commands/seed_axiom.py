from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.axiom.models import AxiomLaw
from sites.axiom.seed_data import law_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Axiom laws (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            AxiomLaw.objects.all().delete()
            b = take_ingested_for_site("axiom", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.axiom_row(ing, i)
                    t = d["enacted_at"]
                    if timezone.is_naive(t):
                        d["enacted_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    AxiomLaw.objects.create(**d)
                    n += 1
            else:
                for row in law_rows():
                    AxiomLaw.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Axiom: {n} laws loaded."))
