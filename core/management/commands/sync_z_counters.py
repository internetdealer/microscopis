from __future__ import annotations

from django.core.management.base import BaseCommand

from core.services.z_counters import sync_z_counters


class Command(BaseCommand):
    help = "Recompute denormalized Z counters (Post likes/reposts, ZProfile followers/following/posts)."

    def handle(self, *args, **options):
        sync_z_counters()
        self.stdout.write(self.style.SUCCESS("Z counters synced from relation tables."))
