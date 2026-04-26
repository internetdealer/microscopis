"""
Copy current ``MEDIA_ROOT/synthetic/{verso|khula|chronicle|z}`` PNGs into
``assets/seed_heroes/`` for committing as pre-rendered seed assets.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

_SUBS = ("verso", "khula", "chronicle", "z")


class Command(BaseCommand):
    help = (
        "Copy media/synthetic bundle PNGs into assets/seed_heroes/ (for git or Git LFS). "
        "Generate images first (e.g. SYNTHETIC_MODE=generate, seed), then run this."
    )

    def handle(self, *args, **options):
        media_root: Path = Path(settings.MEDIA_ROOT)
        out_root: Path = settings.SEED_HEROES_DIR
        n = 0
        for sub in _SUBS:
            src = media_root / "synthetic" / sub
            if not src.is_dir():
                continue
            dest = out_root / sub
            dest.mkdir(parents=True, exist_ok=True)
            for f in sorted(src.glob("*.png")):
                shutil.copy2(f, dest / f.name)
                n += 1
                self.stdout.write(f"  {f.name} -> {dest / f.name}")
        if not n:
            self.stdout.write(
                self.style.WARNING(
                    f"No PNGs under {media_root / 'synthetic'}. "
                    "Run seeds with SYNTHETIC_MODE=generate (and SD if desired) first."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Exported {n} file(s) to {out_root} — review, add Git LFS if needed, then commit."
                )
            )
