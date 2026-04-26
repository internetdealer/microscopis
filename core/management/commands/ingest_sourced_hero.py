import requests
from django.core.management.base import BaseCommand, CommandError

from core.utils.sourced_media import download_hero_to_media


class Command(BaseCommand):
    help = (
        "Download a licensed HTTPS image into media/sourced/{verso|khula}/ and print the public URL. "
        "Use SEED_SOURCED_IMAGE_ALLOW_HOSTS and SEED_SOURCED_IMAGE_MAX_BYTES (see DEPLOY.md)."
    )

    def add_arguments(self, parser):
        parser.add_argument("--url", required=True, help="Direct https:// URL to the image file")
        parser.add_argument(
            "--site",
            required=True,
            choices=["verso", "khula"],
            help="Target subfolder under media/sourced/",
        )
        parser.add_argument(
            "--slug",
            required=True,
            help="Used as filename stem (slugified) under sourced/<site>/",
        )
        parser.add_argument(
            "--credit",
            default="",
            help="Attribution line to echo for pasting into seed (image_credit)",
        )

    def handle(self, *args, **options):
        url = (options.get("url") or "").strip()
        site: str = options["site"]
        slug: str = (options.get("slug") or "").strip()
        credit: str = (options.get("credit") or "").strip()
        if not url:
            raise CommandError("--url is required")
        if not slug:
            raise CommandError("--slug is required")
        try:
            public_url, nbytes = download_hero_to_media(url, site=site, filename_stem=slug)
        except (OSError, ValueError, requests.RequestException) as e:
            raise CommandError(str(e)) from e
        self.stdout.write(self.style.SUCCESS("Downloaded to MEDIA_ROOT:"))
        self.stdout.write(f"  bytes: {nbytes}")
        self.stdout.write(f"  image_url: {public_url}")
        if credit:
            self.stdout.write(f"  image_credit: {credit}")
        else:
            self.stdout.write(
                self.style.WARNING("  Pass --credit with full attribution (license) for your seed data.")
            )
