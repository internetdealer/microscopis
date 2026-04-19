"""Driftglass probes: one row per unique URL in the shared image registry."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone

from core.utils.image_registry import driftglass_probe_dicts


def probe_rows():
    """Rows for DriftglassImage — full network catalog of described images."""
    rows: list[dict] = []
    now = timezone.now()
    for i, d in enumerate(driftglass_probe_dicts()):
        row = dict(d)
        row["created_at"] = now - timedelta(minutes=i * 12)
        rows.append(row)
    return rows
