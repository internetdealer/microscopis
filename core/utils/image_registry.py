"""
Compatibility shim: Driftglass remote image catalog.

Article seeding uses :mod:`core.utils.synthetic_media` and does not import bulk
helpers from this module. The canonical data lives in
:mod:`core.utils.driftglass_image_registry`.
"""

from __future__ import annotations

from core.utils.driftglass_image_registry import (
    IMAGE_REGISTRY,
    all_image_urls,
    driftglass_probe_dicts,
    registry_by_key,
    registry_by_url,
)

__all__ = [
    "IMAGE_REGISTRY",
    "all_image_urls",
    "driftglass_probe_dicts",
    "registry_by_key",
    "registry_by_url",
]
