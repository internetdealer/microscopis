from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from core.ingest import mapping as ingest_mapping
from sites.residue.models import ResidueFragment
from sites.residue.seed_data import fragment_rows
from core.utils.web_seed import take_ingested_for_site

TARGET = 100


class Command(BaseCommand):
    help = "Load Residue fragment data (web-ingested or synthetic fallback)."

    def handle(self, *args, **options):
        with transaction.atomic():
            ResidueFragment.objects.all().delete()
            b = take_ingested_for_site("residue", n=TARGET)
            n = 0
            if b.items is not None:
                for i, ing in enumerate(b.items):
                    d = ingest_mapping.residue_row(ing, i)
                    t = d["archived_at"]
                    if timezone.is_naive(t):
                        d["archived_at"] = timezone.make_aware(
                            t, timezone.get_current_timezone()
                        )
                    ResidueFragment.objects.create(**d)
                    n += 1
            else:
                for row in fragment_rows():
                    ResidueFragment.objects.create(**row)
                    n += 1
        self.stdout.write(self.style.SUCCESS(f"Residue: {n} entries loaded."))
