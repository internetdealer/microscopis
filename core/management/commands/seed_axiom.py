from django.core.management.base import BaseCommand
from django.db import transaction

from sites.axiom.models import AxiomLaw
from sites.axiom.seed_data import law_rows


class Command(BaseCommand):
    help = "Load Axiom laws (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            AxiomLaw.objects.all().delete()
            n = 0
            for row in law_rows():
                AxiomLaw.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Axiom: {n} laws loaded."))
