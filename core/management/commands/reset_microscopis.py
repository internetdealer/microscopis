"""Wipe seeded site rows (articles, posts, driftglass plates, etc.) then re-seed everything."""

from __future__ import annotations

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from sites.axiom.models import AxiomLaw
from sites.chronicle.models import ChronicleEntry, ChronicleTag
from sites.codex.models import CodexEntry
from sites.driftglass.models import DriftglassImage
from sites.errata.models import ErrataCorrection
from sites.gilt.models import GiltEntry
from sites.khula.models import KhulaArticle, KhulaCategory
from sites.parlor.models import ParlorDialogue
from sites.residue.models import ResidueFragment
from sites.sable.models import SableTheory
from sites.static.models import StaticSignal
from sites.vestige.models import VestigeExhibit
from sites.verso.models import VersoArticle, VersoCategory
from sites.z.seed_data import SEED_USERNAMES

User = get_user_model()


class Command(BaseCommand):
    help = (
        "Delete all seeded microscopis content (including Z agent posts and Driftglass rows), "
        "then run seed_microscopis."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-seed",
            action="store_true",
            help="Only flush content; do not run seed_microscopis afterward.",
        )

    def handle(self, *args, **options):
        skip_seed: bool = options["skip_seed"]
        with transaction.atomic():
            User.objects.filter(username__in=SEED_USERNAMES).delete()
            DriftglassImage.objects.all().delete()
            KhulaArticle.objects.all().delete()
            KhulaCategory.objects.all().delete()
            VersoArticle.objects.all().delete()
            VersoCategory.objects.all().delete()
            ChronicleEntry.objects.all().delete()
            ChronicleTag.objects.all().delete()
            GiltEntry.objects.all().delete()
            ParlorDialogue.objects.all().delete()
            StaticSignal.objects.all().delete()
            ResidueFragment.objects.all().delete()
            ErrataCorrection.objects.all().delete()
            AxiomLaw.objects.all().delete()
            CodexEntry.objects.all().delete()
            SableTheory.objects.all().delete()
            VestigeExhibit.objects.all().delete()
            # Z: deleting seed agent users cascades posts, likes, reposts, follows, profiles for those users only.

        self.stdout.write(
            self.style.WARNING(
                "Flushed seeded site tables and seed-agent Z accounts (other users’ posts are untouched)."
            )
        )
        if not skip_seed:
            call_command("seed_microscopis")
            self.stdout.write(self.style.SUCCESS("Re-ran seed_microscopis."))
