"""Lightweight consistency checks for Driftglass vs the shared remote image catalog."""

from __future__ import annotations

from django.core.management.base import BaseCommand

from core.utils.driftglass_image_registry import IMAGE_REGISTRY, all_image_urls
from sites.driftglass.models import DriftglassImage


class Command(BaseCommand):
    help = (
        "Compare canonical Driftglass registry image URLs to DriftglassImage DB rows. "
        "Use after seed_driftglass. Optional --strict exits non-zero if URLs are missing. "
        "Optional --check-themes flags registry content_themes coverage."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--strict",
            action="store_true",
            help="Exit with code 1 if any registry URL is missing from DriftglassImage.",
        )
        parser.add_argument(
            "--check-themes",
            action="store_true",
            help="Verify every Driftglass registry row has content_themes (article heroes are not checked).",
        )

    def handle(self, *args, **options):
        strict: bool = options["strict"]
        check_themes: bool = options["check_themes"]
        expected = set(all_image_urls())
        db_urls = set(DriftglassImage.objects.values_list("image_url", flat=True))
        missing = expected - db_urls
        extra = db_urls - expected
        theme_mismatch = False

        self.stdout.write(f"Unique URLs in Driftglass IMAGE_REGISTRY: {len(expected)}")
        self.stdout.write(f"Registry list length (after dedupe pass): {len(IMAGE_REGISTRY)}")
        self.stdout.write(f"DriftglassImage rows: {DriftglassImage.objects.count()}")

        if check_themes:
            for e in IMAGE_REGISTRY:
                if not (e.get("content_themes") or []):
                    self.stdout.write(
                        self.style.ERROR(f"Registry row {e.get('key')!r} has no content_themes.")
                    )
                    theme_mismatch = True
            if not theme_mismatch:
                self.stdout.write(
                    self.style.SUCCESS("Theme check: all Driftglass registry rows have content_themes.")
                )
            elif not strict:
                self.stdout.write(
                    self.style.NOTICE("Theme check reported issues (see above). Use --strict to fail the command.")
                )

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
        if strict and check_themes and theme_mismatch:
            self.stderr.write(
                self.style.ERROR("Strict mode: fix Driftglass registry content_themes.")
            )
            raise SystemExit(1)
