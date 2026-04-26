"""Celery tasks (imported from core.apps CoreConfig.ready so registration runs after apps load)."""
from __future__ import annotations

from celery import shared_task

from core.services.z_counters import sync_z_counters as _sync_z_counters


@shared_task
def sync_z_counters() -> None:
    _sync_z_counters()
