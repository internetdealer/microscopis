from django.core.management.base import BaseCommand
from django.db import transaction

from sites.driftglass.models import DriftglassImage
from core.utils.image_urls import ensure_reachable_image_url
from sites.driftglass.seed_data import probe_rows


class Command(BaseCommand):
    help = "Load Driftglass image probes (replaces existing rows)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--verify-images",
            action="store_true",
            help="HTTP-check each probe image URL and substitute a fallback if unreachable (slower).",
        )

    def handle(self, *args, **options):
        verify = options.get("verify_images")
        warn = (
            (lambda m: self.stdout.write(self.style.WARNING(m))) if verify else None
        )

        with transaction.atomic():
            DriftglassImage.objects.all().delete()
            n = 0
            for row in probe_rows():
                payload = dict(row)
                if verify:
                    payload["image_url"] = ensure_reachable_image_url(
                        payload["image_url"], warn
                    )
                DriftglassImage.objects.create(**payload)
                n += 1

        self.stdout.write(self.style.SUCCESS(f"Driftglass: {n} probes loaded."))
