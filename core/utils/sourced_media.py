"""
Download a licensed hero image from HTTPS into ``MEDIA_ROOT/sourced/{site}/`` for same-origin URLs.

Host allowlist and size limits are controlled with environment variables (see ``ingest_sourced_hero``).
"""

from __future__ import annotations

import hashlib
import os
from io import BytesIO
from typing import Any
from urllib.parse import unquote, urlparse

import requests
from django.conf import settings

from core.utils.synthetic_media import public_url_for_path, _slugify

# Default when SEED_SOURCED_IMAGE_ALLOW_HOSTS is unset: common open-license CDNs
_DEFAULT_ALLOWED_HOSTS: frozenset[str] = frozenset(
    {
        "upload.wikimedia.org",
        "commons.wikimedia.org",
        "images.unsplash.com",
    }
)
_ALLOWED_CTYPES = frozenset(
    {
        "image/jpeg",
        "image/jpg",
        "image/png",
        "image/webp",
    }
)

EXT_FOR_CT: dict[str, str] = {
    "image/jpeg": "jpg",
    "image/jpg": "jpg",
    "image/png": "png",
    "image/webp": "webp",
}


def _max_bytes() -> int:
    try:
        return int(os.environ.get("SEED_SOURCED_IMAGE_MAX_BYTES", "5000000"))
    except ValueError:
        return 5_000_000


def _host_allowset() -> frozenset[str] | None:
    """
    None = do not check host (SEED_SOURCED_IMAGE_ALLOW_HOSTS=* only).
    Empty string from env: use _DEFAULT_ALLOWED_HOSTS.
    """
    raw = (os.environ.get("SEED_SOURCED_IMAGE_ALLOW_HOSTS", "") or "").strip()
    if raw == "*":
        return None
    if not raw:
        return _DEFAULT_ALLOWED_HOSTS
    return frozenset(h.strip().lower() for h in raw.split(",") if h.strip())


def _assert_allowed_url(url: str) -> str:
    p = urlparse(url)
    if p.scheme != "https":
        raise ValueError("Only https:// image URLs are allowed")
    if not p.netloc:
        raise ValueError("Invalid image URL")
    host = p.hostname
    if not host:
        raise ValueError("URL has no host")
    allow = _host_allowset()
    h = host.lower()
    if allow is not None and h not in allow:
        raise ValueError(
            f"Host {h!r} not in allowlist. Set SEED_SOURCED_IMAGE_ALLOW_HOSTS or use a default-allowed host."
        )
    return url


def download_hero_to_media(
    image_url: str,
    *,
    site: str,
    filename_stem: str,
) -> tuple[str, int]:
    """
    Download ``image_url`` to ``MEDIA_ROOT/sourced/{site}/{filename_stem}.{ext}``.

    Returns ``(same_origin_media_path_url, bytes_written)`` (see ``synthetic_media.public_url_for_path``).
    """
    if site not in ("verso", "khula"):
        raise ValueError("site must be 'verso' or 'khula'")
    url = _assert_allowed_url(image_url.strip())
    max_b = _max_bytes()
    timeout = int(os.environ.get("SEED_SOURCED_IMAGE_TIMEOUT", "60"))
    r = requests.get(
        url,
        stream=True,
        timeout=timeout,
        headers={"User-Agent": "microscopis-seed/1.0 (sourced image ingest)"},
    )
    r.raise_for_status()
    ct = (r.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    if ct and ct not in _ALLOWED_CTYPES:
        raise ValueError(f"Unsupported Content-Type: {ct!r} (expected jpeg, png, or webp)")
    buf = BytesIO()
    n = 0
    for chunk in r.iter_content(chunk_size=65536):
        if not chunk:
            break
        n += len(chunk)
        if n > max_b:
            raise ValueError(f"Image larger than SEED_SOURCED_IMAGE_MAX_BYTES ({max_b})")
        buf.write(chunk)
    data = buf.getvalue()
    if len(data) < 64:
        raise ValueError("Downloaded file too small to be a valid image")
    if not ct:
        path_part = unquote(urlparse(url).path)
        if path_part.lower().endswith(".png"):
            ext = "png"
        elif path_part.lower().endswith((".jpg", ".jpeg")):
            ext = "jpg"
        elif path_part.lower().endswith(".webp"):
            ext = "webp"
        else:
            ext = "jpg"
    else:
        ext = EXT_FOR_CT[ct]
    safe_stem = _slugify(filename_stem) or "hero"
    media_root: Any = settings.MEDIA_ROOT
    out_dir = media_root / "sourced" / site
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{safe_stem}.{ext}"
    out_path = out_dir / filename
    out_path.write_bytes(data)
    rel = f"sourced/{site}/{filename}"
    v = hashlib.sha256(data).hexdigest()[:10]
    return public_url_for_path(rel, cache_bust=v), len(data)
