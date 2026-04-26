"""
Fetch HTML, extract main text and hero image, save image under ``MEDIA_ROOT`` for :class:`IngestedArticle`.
"""

from __future__ import annotations

import hashlib
import os
import re
from io import BytesIO
from typing import Any
from urllib.parse import unquote, urljoin, urlparse

import httpx
import trafilatura
from bs4 import BeautifulSoup
from django.conf import settings

# --- env ---------------------------------------------------------------------------

def _bool(name: str, default: bool = False) -> bool:
    v = (os.environ.get(name) or "").lower()
    if v in ("1", "true", "yes", "on"):
        return True
    if v in ("0", "false", "no", "off"):
        return False
    return default


def image_allow_all_hosts() -> bool:
    return _bool("INGEST_IMAGE_ALLOW_ALL", default=True)


def _max_image_bytes() -> int:
    try:
        return int(os.environ.get("INGEST_IMAGE_MAX_BYTES", "8000000"))
    except ValueError:
        return 8_000_000


_USER_AGENT = os.environ.get(
    "INGEST_USER_AGENT",
    "microscopis-web-ingest/1.0 (+https://github.com/; local corpus seed)",
)

_TIMEOUT = float(os.environ.get("INGEST_HTTP_TIMEOUT", "40"))


def _client() -> httpx.Client:
    return httpx.Client(
        follow_redirects=True,
        timeout=_TIMEOUT,
        headers={"User-Agent": _USER_AGENT, "Accept": "text/html,application/xhtml+xml"},
    )


def _norm_body_hash(text: str | None) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip())
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def extract_og_image_url(html: str, base_url: str) -> str | None:
    if not html:
        return None
    soup = BeautifulSoup(html, "lxml")
    for prop in ("og:image", "twitter:image:src", "og:image:secure_url"):
        tag = soup.find("meta", property=prop)
        if tag and tag.get("content"):
            return urljoin(base_url, tag["content"].strip())
        tag2 = soup.find("meta", attrs={"name": prop})
        if tag2 and tag2.get("content"):
            return urljoin(base_url, tag2["content"].strip())
    return None


def download_image_to_media(
    image_url: str, *, subdir: str, stem: str
) -> tuple[str, str] | None:
    """
    Return ``(image_media_relpath, public_url)`` e.g. (``sourced/ingest/…/a.jpg``, ``/media/...``)
    or None on failure. Relaxes host policy when :envvar:`INGEST_IMAGE_ALLOW_ALL` is true.
    """
    if not (image_url or "").strip().startswith(("http://", "https://")):
        return None
    p = urlparse(image_url)
    if p.scheme not in ("http", "https") or not p.netloc:
        return None
    if not image_allow_all_hosts():
        from core.utils.sourced_media import _assert_allowed_url  # private but matches policy

        try:
            _assert_allowed_url(image_url)
        except ValueError:
            return None
    ext = "jpg"
    path_part = unquote(urlparse(image_url).path)
    for cand in (".png", ".webp", ".gif", ".jpeg", ".jpg"):
        if path_part.lower().endswith(cand):
            ext = "jpeg" if cand == ".jpeg" else cand[1:].lower()
            break
    try:
        with _client() as c:
            r = c.get(image_url, timeout=_TIMEOUT)
            r.raise_for_status()
            data = r.content
            if not data or len(data) < 32 or len(data) > _max_image_bytes():
                return None
            ct = (r.headers.get("Content-Type") or "").split(";")[0].strip().lower()
            if "png" in ct:
                ext = "png"
            elif "webp" in ct:
                ext = "webp"
            elif "gif" in ct:
                ext = "gif"
    except (OSError, httpx.HTTPError, ValueError):
        return None
    h = hashlib.sha256(data).hexdigest()[:12]
    media_root: Any = settings.MEDIA_ROOT
    out_dir = media_root / "sourced" / "ingest" / f"{subdir}-{h[:8]}"
    out_dir.mkdir(parents=True, exist_ok=True)
    fn = f"{stem}.{ext}"
    path = out_dir / fn
    path.write_bytes(data)
    rel = f"sourced/ingest/{subdir}-{h[:8]}/{fn}"
    from core.utils.synthetic_media import public_url_for_path

    v = hashlib.sha256(data).hexdigest()[:10]
    url = public_url_for_path(rel, cache_bust=v)
    return rel, url


def fetch_page(url: str) -> tuple[str | None, str | None]:
    """Return ``(html, final_url)`` or ``(None, None)``."""
    try:
        with _client() as c:
            r = c.get(url, timeout=_TIMEOUT, follow_redirects=True)
            r.raise_for_status()
            ct = (r.headers.get("Content-Type") or "").lower()
            if "html" not in ct and "xml" not in ct:
                return None, None
            return r.text, str(r.url)
    except (OSError, httpx.HTTPError, UnicodeDecodeError):
        return None, None


def extract_article_from_url(url: str) -> dict[str, Any] | None:
    """
    Return dict with title, body, excerpt, author_line, image_media_relpath, image_credit,
    source_image_url, or None.
    """
    html, final_url = fetch_page(url)
    if not html or not final_url:
        return None
    text = trafilatura.extract(
        html,
        url=final_url,
        include_comments=False,
        include_tables=True,
        include_links=False,
        favor_recall=True,
    )
    if not (text and len(text.strip()) > 200):
        return None
    try:
        meta = trafilatura.extract_metadata(html, default_url=final_url)
    except (TypeError, ValueError, AttributeError, OSError):
        meta = None
    title = (getattr(meta, "title", None) or "").strip() if meta else ""
    if not title:
        m2 = re.search(r"<title[^>]*>([^<]{5,200})", html, re.I)
        title = m2.group(1).strip() if m2 else final_url
    title = re.sub(r"\s+", " ", title)[:500]
    author = ""
    if meta:
        author = (getattr(meta, "author", None) or getattr(meta, "sitename", None) or "").strip()[:400]
    excerpt = (text[:500] + "…") if len(text) > 500 else text
    ex = re.sub(r"\s+", " ", excerpt)[:2000]

    img_url = extract_og_image_url(html, final_url)
    if not img_url and meta and getattr(meta, "image", None):
        img_url = (meta.image or "").strip() or None
    if img_url and not str(img_url).startswith("http"):
        img_url = urljoin(final_url, str(img_url))

    stem = hashlib.sha256(final_url.encode()).hexdigest()[:10]
    rel = None
    credit = author or urlparse(final_url).hostname or "Source"
    if img_url:
        got = download_image_to_media(
            str(img_url), subdir=stem, stem="hero"
        )
        if got:
            rel, _ = got
    pub = None
    if meta and getattr(meta, "date", None):
        d = meta.date
        from datetime import date as date_cls, datetime as dt_cls

        from django.utils import timezone as django_tz

        if isinstance(d, dt_cls):
            pub = django_tz.make_aware(d) if django_tz.is_naive(d) else d
        elif isinstance(d, date_cls):
            from datetime import time as time_cls

            t0 = time_cls(12, 0, 0)
            dd = dt_cls.combine(d, t0)
            pub = django_tz.make_aware(dd)
    return {
        "title": title,
        "body": text,
        "excerpt": ex,
        "author_line": author,
        "image_media_relpath": rel or "",
        "image_credit": credit[:500] if rel else "No image (text only)",
        "source_image_url": (str(img_url) if img_url else "")[:2000],
        "published_at": pub,
    }


