from django.core.management.base import BaseCommand
from django.db import transaction

from sites.codex.models import CodexEntry
from sites.codex.seed_data import entry_rows


class Command(BaseCommand):
    help = "Load Codex entries (replaces existing rows)."

    def handle(self, *args, **options):
        with transaction.atomic():
            CodexEntry.objects.all().delete()
            n = 0
            for row in entry_rows():
                CodexEntry.objects.create(**row)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Codex: {n} entries loaded."))
