"""Lightweight consistency checks for seeded content and the shared image registry."""

from __future__ import annotations

from django.core.management.base import BaseCommand

from core.utils.image_registry import IMAGE_REGISTRY, all_image_urls
from sites.driftglass.models import DriftglassImage


class Command(BaseCommand):
    help = (
        "Compare canonical registry image URLs to Driftglass rows. "
        "Use after seed_driftglass. Optional --strict exits non-zero if URLs are missing."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--strict",
            action="store_true",
            help="Exit with code 1 if any registry URL is missing from DriftglassImage.",
        )

    def handle(self, *args, **options):
        strict: bool = options["strict"]
        expected = set(all_image_urls())
        db_urls = set(DriftglassImage.objects.values_list("image_url", flat=True))
        missing = expected - db_urls
        extra = db_urls - expected

        self.stdout.write(f"Unique URLs in IMAGE_REGISTRY: {len(expected)}")
        self.stdout.write(f"Registry list length (after dedupe pass): {len(IMAGE_REGISTRY)}")
        self.stdout.write(f"DriftglassImage rows: {DriftglassImage.objects.count()}")

        if missing:
            sample = ", ".join(sorted(missing)[:6])
            more = " …" if len(missing) > 6 else ""
            self.stdout.write(
                self.style.WARNING(
                    f"Registry URLs with no Driftglass row ({len(missing)}): {sample}{more}"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Every registry URL has a matching Driftglass row.")
            )

        if extra:
            self.stdout.write(
                self.style.NOTICE(
                    f"Driftglass URLs not in current registry module: {len(extra)} (often harmless if DB is stale)."
                )
            )

        if strict and missing:
            self.stderr.write(
                self.style.ERROR("Strict mode: re-run seed_driftglass or fix the registry.")
            )
            raise SystemExit(1)
