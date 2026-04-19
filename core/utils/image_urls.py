"""Verify remote image URLs before writing them from seed commands."""

from __future__ import annotations

import ssl
import urllib.error
import urllib.request

DEFAULT_USER_AGENT = (
    "Microscopis/1.0 (+https://example.invalid; Django seed; image URL check)"
)

# Curated list: verified HTTP 200 + image/* (HEAD). Used when primary URL fails.
VERIFIED_FALLBACK_IMAGES: tuple[str, ...] = (
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=1600&q=80",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg",
)


def _ssl_context() -> ssl.SSLContext:
    return ssl.create_default_context()


def image_url_reachable(url: str, *, timeout: float = 22.0) -> bool:
    """Return True if the URL responds with 200 and (likely) serves an image."""
    if not url or not url.startswith(("http://", "https://")):
        return False
    ctx = _ssl_context()
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": DEFAULT_USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            if resp.status != 200:
                return False
            ct = (resp.headers.get("Content-Type") or "").lower()
            return "image" in ct or ct == ""
    except urllib.error.HTTPError as exc:
        if exc.code == 405:
            return _image_get_probe(url, timeout=timeout, ctx=ctx)
        return False
    except OSError:
        return _image_get_probe(url, timeout=timeout, ctx=ctx)


def _image_get_probe(url: str, *, timeout: float, ctx: ssl.SSLContext) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": DEFAULT_USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            if resp.status != 200:
                return False
            ct = (resp.headers.get("Content-Type") or "").lower()
            if "image" in ct:
                return True
            chunk = resp.read(512)
            return len(chunk) > 32
    except OSError:
        return False


def ensure_reachable_image_url(
    url: str,
    style_warning=None,
    *,
    timeout: float = 22.0,
) -> str:
    """
    Return ``url`` if it responds OK; otherwise the first working fallback.

    ``style_warning`` is optional ``BaseCommand.style.WARNING`` (or any callable
    taking a string) used to log substitutions when the primary URL fails.
    """
    cleaned = (url or "").strip()
    if not cleaned:
        return ""
    if image_url_reachable(cleaned, timeout=timeout):
        return cleaned
    if style_warning is not None:
        style_warning(f"Image unreachable, using fallback ({cleaned[:72]}…)")
    # Rotate starting point so a batch of bad URLs do not all map to the same photo.
    n = len(VERIFIED_FALLBACK_IMAGES)
    start = sum(ord(c) for c in cleaned[:200]) % n if cleaned else 0
    for i in range(n):
        fb = VERIFIED_FALLBACK_IMAGES[(start + i) % n]
        if image_url_reachable(fb, timeout=timeout):
            return fb
    return VERIFIED_FALLBACK_IMAGES[0]
