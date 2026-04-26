"""
Partition :class:`IngestedArticle` rows (``INGEST_OMNI_POOL``) across ~100-row site seeds and
synthetic fallbacks.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, List, TypeVar

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet

from core.models import IngestedArticle

T = TypeVar("T")

ROWS_PER_SITE = 100


@dataclass
class IngestBatch:
    items: list[IngestedArticle] | None
    used_fallback: bool
    count: int


def _pool_qs() -> QuerySet[IngestedArticle]:
    return IngestedArticle.objects.filter(
        pool=(getattr(settings, "INGEST_OMNI_POOL", "omni") or "omni")
    ).order_by("id")


def site_partition_index(website_key: str) -> int:
    try:
        return list(settings.INGEST_PARTITION_SITE_ORDER).index(website_key)
    except ValueError as e:
        raise ImproperlyConfigured(
            f"Unknown site key {website_key!r} for INGEST partition"
        ) from e


def take_ingested_for_site(website_key: str, *, n: int = ROWS_PER_SITE) -> IngestBatch:
    """
    Return the next ``n`` ingested articles for this site's slice, or None + fallback flag
    if the table is too small and ``USE_SYNTHETIC_SEED_FALLBACK`` is true.
    """
    start = site_partition_index(website_key) * n
    all_rows: list[IngestedArticle] = list(_pool_qs())
    need = start + n
    if len(all_rows) >= need:
        return IngestBatch(
            items=all_rows[start : start + n], used_fallback=False, count=n
        )
    if getattr(settings, "USE_SYNTHETIC_SEED_FALLBACK", True):
        return IngestBatch(items=None, used_fallback=True, count=0)
    raise ImproperlyConfigured(
        f"Need at least {need} IngestedArticle rows (pool={settings.INGEST_OMNI_POOL!r}) to seed "
        f"{website_key!r} (slice [{start}:{need}]), but the pool has {len(all_rows)}. "
        f"Run `python manage.py ingest_web_corpus` (target 1300+ for all sites) or set "
        f"USE_SYNTHETIC_SEED_FALLBACK=1."
    )


def or_fallback(
    fn_ing: Callable[[List[IngestedArticle]], T],
    fn_synth: Callable[[], T],
    website_key: str,
) -> T:
    """Run mapper on ingested batch or the synthetic callback."""
    b = take_ingested_for_site(website_key)
    if b.items is not None:
        return fn_ing(b.items)
    return fn_synth()
