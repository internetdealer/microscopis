"""
Map :class:`core.models.IngestedArticle` rows into each site’s model kwargs.
"""

from __future__ import annotations

import hashlib
import re
from datetime import date, datetime, timedelta
from typing import Any
from urllib.parse import urlparse

from django.utils import timezone
from django.utils.text import slugify

from core.models import IngestedArticle
from core.utils.synthetic_media import public_url_for_path


def _slug(prefix: str, ing: IngestedArticle) -> str:
    base = slugify(ing.title)[:70] or "doc"
    suf = hashlib.sha256(f"{ing.id}-{ing.source_url}".encode()).hexdigest()[:8]
    s = f"{prefix}-{base}-{suf}"
    return s[:128]


def _img(ing: IngestedArticle) -> tuple[str, str]:
    rel = (ing.image_media_relpath or "").strip()
    if not rel:
        return "", "No image"
    v = (ing.content_hash or "")[:10] or str(ing.id)
    return public_url_for_path(rel, cache_bust=v), (ing.image_credit or "Source")[:255]


def verso_rows(ing: IngestedArticle, *, category_slug: str, read_minutes: int, is_featured: bool) -> dict[str, Any]:
    img, cred = _img(ing)
    pub = ing.published_at.date() if ing.published_at else date(2024, 1, 1)
    return {
        "slug": _slug("v", ing),
        "title": ing.title[:255],
        "excerpt": (ing.excerpt or ing.body[:400])[:2000],
        "body": ing.body,
        "author": (ing.author_line[:128] if ing.author_line else "Wire") or "Wire",
        "published_at": pub,
        "read_minutes": read_minutes,
        "is_featured": is_featured,
        "image_url": img,
        "image_credit": cred,
        "_category_slug": category_slug,
    }


def khula_rows(ing: IngestedArticle, *, category_slug: str, read_minutes: int, is_featured: bool) -> dict[str, Any]:
    img, cred = _img(ing)
    pub = ing.published_at.date() if ing.published_at else date(2024, 1, 1)
    ex = ing.excerpt or ing.body[:400]
    ex = (
        "Illustrative stock photo—not from the collection or runway named below. "
        + ex
    )[:4000]
    return {
        "slug": _slug("k", ing),
        "title": ing.title[:255],
        "excerpt": ex,
        "body": ing.body,
        "author": (ing.author_line[:128] if ing.author_line else "Khula_Agent") or "Khula_Agent",
        "published_at": pub,
        "read_minutes": read_minutes,
        "is_featured": is_featured,
        "image_url": img,
        "image_credit": cred,
        "_category_slug": category_slug,
    }


def chronicle_entry(ing: IngestedArticle, i: int, tags: list[str]) -> dict[str, Any]:
    img, cred = _img(ing)
    moods = ["focused", "tired", "wired", "calm", "sharp", "soft"]
    m = moods[i % len(moods)]
    tag0 = tags[i % len(tags)]
    tag1 = tags[(i + 2) % len(tags)]
    pub = ing.published_at or timezone.now() - timedelta(hours=i)
    return {
        "slug": _slug("ch", ing),
        "title": ing.title[:255],
        "excerpt": (ing.excerpt or ing.body[:300])[:2000],
        "body": ing.body,
        "author_name": (ing.author_line[:128] if ing.author_line else "Chronicle_Agent") or "Chronicle_Agent",
        "author_handle": f"log_{ing.id % 8000}",
        "mood": m.title(),
        "mood_emoji": "◆",
        "current_music": "field audio / link",
        "location": (urlparse(ing.source_url).hostname or "edge")[:255],
        "published_at": pub,
        "image_url": img,
        "image_credit": cred,
        "display_likes": i % 200,
        "tags": [tag0, tag1],
    }


def gilt_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    name = "Aurora Vale"
    if ing.author_line:
        parts = re.split(r"[,;]", ing.author_line)
        cand = (parts[0] or "").strip()
        if 3 < len(cand) < 100:
            name = cand[:120]
    moods = ["paranoid", "triumphant", "bored", "vengeful", "nostalgic"]
    pub = ing.published_at.date() if ing.published_at else date(2025, 1, 10)
    return {
        "slug": _slug("gl", ing),
        "billionaire_name": name,
        "title": ing.title[:200],
        "body": ing.body,
        "mood_tag": moods[i % len(moods)],
        "is_featured": i % 12 == 0,
        "entry_date": pub,
    }


def parlor_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    pairs = [
        ("Ada Lovelace", "Grace Hopper"),
        ("Alan Turing", "John von Neumann"),
        ("Hypatia", "Marie Curie"),
        ("Kafka", "Borges"),
        ("Sun Tzu", "Clausewitz"),
    ]
    a, b = pairs[i % len(pairs)]
    paras = [p.strip() for p in re.split(r"\n\s*\n", ing.body) if p.strip()]
    if len(paras) < 2:
        half = len(ing.body) // 2
        left, right = ing.body[:half], ing.body[half:]
    else:
        m = max(1, len(paras) // 2)
        left = "\n\n".join(paras[:m])
        right = "\n\n".join(paras[m:])
    body = f"[{a}]\n\n{left}\n\n[{b}]\n\n{right}"
    return {
        "slug": _slug("parlor", ing),
        "title": (ing.title[:200] if len(ing.title) < 200 else ing.title[:197] + "…"),
        "person_a": a,
        "person_b": b,
        "body": body[:50000],
        "is_featured": i % 15 == 0,
        "created_at": ing.published_at or timezone.now() - timedelta(days=i),
    }


def static_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    types = ["numbers", "broadcast", "deep_space", "unknown"]
    t = types[i % len(types)]
    return {
        "slug": _slug("sig", ing),
        "designation": f"SIG-{i:04d}-WEB",
        "signal_type": t,
        "origin_description": (urlparse(ing.source_url).hostname or "unknown")[:200],
        "transcript": ing.body[:8000],
        "analysis_notes": (ing.excerpt or "")[:2000],
        "is_featured": i % 18 == 0,
        "intercepted_at": ing.published_at or timezone.now() - timedelta(hours=i * 2),
    }


def residue_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    types = ["page", "post", "comment", "profile", "listing"]
    return {
        "slug": _slug("frag", ing),
        "original_url": ing.source_url[:300],
        "fragment_type": types[i % len(types)],
        "site_name": (urlparse(ing.source_url).hostname or f"site-{i}")[:120],
        "recovered_text": ing.body[:20000],
        "context_notes": ing.excerpt[:1000] if ing.excerpt else "",
        "is_featured": i % 20 == 0,
        "archived_at": ing.published_at or timezone.now() - timedelta(days=i),
    }


def errata_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    sev = ["minor", "major", "critical", "retraction"]
    return {
        "slug": _slug("err", ing),
        "original_claim": ing.title[:300],
        "correction": ing.body[:20000],
        "severity": sev[i % len(sev)],
        "source_cited": (urlparse(ing.source_url).hostname or "web")[:200],
        "editor_note": "Derived from a current web article in this demo database.",
        "fact_year": 1990 + (i % 35),
        "wikipedia_url": (ing.source_url if ing.source_url.startswith("https://") and len(ing.source_url) <= 500 else "")[
            :500
        ],
        "is_featured": i % 14 == 0,
        "issued_at": ing.published_at or timezone.now() - timedelta(days=i),
    }


def axiom_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    laws = ["constitution", "statute", "ruling", "amendment"]
    inst = ["EU AI Act", "NIST AI RMF", "OECD AI Principles", "GDPR Art. 22", "ISO/IEC 42001"]
    pub = ing.published_at or timezone.now()
    return {
        "slug": _slug("law", ing),
        "civilization_name": inst[i % len(inst)][:120],
        "law_type": laws[i % len(laws)],
        "title": ing.title[:200],
        "body": ing.body[:50000],
        "article_number": f"§{i % 50}",
        "is_featured": i % 16 == 0,
        "enacted_at": pub,
    }


def codex_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    ety = ["word", "phrase", "grammar", "poem"]
    lang = f"Lingua-{i % 24}"
    term = ing.title[:200]
    ch0 = term[0] if term else "A"
    letter = ch0.upper() if ch0.isalpha() else "A"
    return {
        "slug": _slug("cx", ing),
        "language_name": lang[:120],
        "entry_type": ety[i % len(ety)],
        "term": term,
        "definition": ing.body[:20000],
        "pronunciation": "",
        "etymology": (ing.excerpt or "")[:2000],
        "letter": letter[:1],
        "is_featured": i % 17 == 0,
        "created_at": ing.published_at or timezone.now() - timedelta(days=i),
    }


def sable_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    pl = ["low", "medium", "high", "unsettling"]
    pub = ing.published_at or timezone.now()
    return {
        "slug": _slug("sb", ing),
        "title": ing.title[:200],
        "plausibility": pl[i % len(pl)],
        "body": ing.body[:20000],
        "evidence_cited": (ing.excerpt or "")[:2000],
        "real_events": (ing.author_line or "")[:2000],
        "wikipedia_urls": ing.source_url[:2000] if len(ing.source_url) <= 2000 else ing.source_url[:1997] + "…",
        "is_featured": i % 13 == 0,
        "published_at": ing.published_at or timezone.now() - timedelta(days=i),
    }


def z_post_from_ing(ing: IngestedArticle, i: int, usernames: list[str]) -> dict[str, Any]:
    img, _cred = _img(ing)
    u = usernames[i % len(usernames)]
    body = (ing.title + "\n\n" + (ing.excerpt or ing.body[:500]))[:2000]
    return {
        "username": u,
        "body": body,
        "media_url": img,
        "parent_index": None,
        "quoted_index": None,
    }


def vestige_row(ing: IngestedArticle, i: int) -> dict[str, Any]:
    ex = ["meme", "site", "trend", "project", "person"]
    return {
        "slug": _slug("vx", ing),
        "title": ing.title[:200],
        "exhibit_type": ex[i % len(ex)],
        "era_desc": f"{2005 + (i % 20)}s",
        "body": ing.body[:20000],
        "last_seen": (ing.author_line or "Web")[:120],
        "wikipedia_url": (ing.source_url if ing.source_url.startswith("https://") and len(ing.source_url) <= 500 else "")[:500],
        "is_featured": i % 11 == 0,
        "curated_at": ing.published_at or timezone.now() - timedelta(days=i),
    }
