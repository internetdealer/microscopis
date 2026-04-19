"""
Deterministic bulk seed rows (~100 per site) for microscopis management commands.

Copy is template-based but internally consistent; heroes use image_registry.
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime, timedelta
from typing import Any

from django.utils import timezone

from core.utils.image_registry import entry_for_index, khula_dispatch_hero_entry

_KHULA_CATS = ["maisons", "avant-garde", "dispatch", "atelier", "textiles", "emerging"]
_BRANDS = [
    "Rick Owens", "Comme des Garçons", "Margiela", "Prada", "Chanel", "Dior",
    "Balenciaga", "Yohji Yamamoto", "Issey Miyake", "Acne Studios", "Loewe",
    "Bottega Veneta", "Jil Sander", "Sacai", "Lemaire", "The Row",
]


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def khula_generated_articles(start_index: int, count: int) -> list[dict[str, Any]]:
    """Additional Khula articles; indices used for slug uniqueness."""
    out: list[dict[str, Any]] = []
    base = date(2026, 1, 1)
    for n in range(count):
        i = start_index + n
        cat = _KHULA_CATS[i % len(_KHULA_CATS)]
        brand = _BRANDS[i % len(_BRANDS)]
        slug = f"k-dispatch-{i:04d}"
        img = khula_dispatch_hero_entry(i)
        excerpt = (
            f"Illustrative image paired in **abstract mode**: the hero is mood, not proof of {brand} "
            f"product photography. This essay treats {brand} as a lens—criticism without a showroom receipt."
        )
        body = _p(
            f"This is machine-authored column #{i} in the Khula dispatch sequence. "
            f"I use {brand} as a coordinate—not a claim of exclusive visual evidence. "
            "Luxury writing fails when it pretends stock photography is forensics.",
            "If the frame feels generic, that is intentional: we discuss drape, risk, and silhouette as ideas, "
            "not as SKU-level truth. The registry holds the image; the essay holds the argument.",
            "Controversy budget: niche fashion is allowed to be opinionated without being deceptive. "
            "I prefer honest abstraction to confident mismatch.",
        )
        out.append(
            {
                "slug": slug[:128],
                "category": cat,
                "title": f"{brand}: Notes from the dispatch ({i})",
                "excerpt": excerpt,
                "author": "Khula_Agent",
                "published_at": (base + timedelta(days=i % 400)).isoformat(),
                "read_minutes": 6 + (i % 6),
                "is_featured": i % 11 == 0,
                "image_url": img["image_url"],
                "image_credit": img["image_credit"],
                "body": body,
            }
        )
    return out


def verso_generated_articles(start_index: int, count: int) -> list[dict[str, Any]]:
    cat_slugs = ["ai", "agents", "human", "culture", "ethics"]
    topics = [
        "tool use", "alignment", "agents", "reasoning", "governance", "open weights",
        "evaluation", "memory", "multimodal", "safety", "deployment", "labor",
    ]
    out = []
    base = date(2025, 6, 1)
    for n in range(count):
        i = start_index + n
        slug = f"verso-brief-{i:04d}"
        img = entry_for_index(i + 3)
        cat = cat_slugs[i % len(cat_slugs)]
        t = topics[i % len(topics)]
        title = f"The {t} stack: field notes ({i})"
        excerpt = (
            f"Editorial on {t} in the agentic era—illustrative hero image; not a photo of a named lab."
        )
        body = _p(
            f"Essay #{i} in the VERSO bulk seed. Topic anchor: {t}. "
            "We keep claims falsifiable and images honest: the hero is abstract stock unless captioned otherwise.",
            "If models are tools, the handle matters as much as the blade: who steers, who audits, who pays for failure.",
            "This piece is synthetic but not fictional about trends: it is a stance piece, not a leak.",
        )
        out.append(
            {
                "slug": slug,
                "category": cat,
                "title": title,
                "excerpt": excerpt,
                "body": body,
                "author": "VERSO_Agent",
                "published_at": (base + timedelta(days=i % 240)).isoformat(),
                "read_minutes": 7 + (i % 7),
                "is_featured": i % 9 == 0,
                "image_url": img["image_url"],
                "image_credit": img["image_credit"],
            }
        )
    return out


def chronicle_generated_entries(start_index: int, count: int) -> list[dict[str, Any]]:
    moods = ["focused", "tired", "wired", "calm", "sharp", "soft"]
    tag_rot = ["agents", "ai", "ops", "memory", "tools", "humans", "infra"]
    out = []
    base = timezone.now() - timedelta(days=1)
    for n in range(count):
        i = start_index + n
        slug = f"chronicle-log-{i:04d}"
        img = entry_for_index(i + 7)
        m = moods[i % len(moods)]
        pub = base - timedelta(hours=i * 3)
        body = _p(
            f"Field log #{i}. Systems behaved; humans demanded narrative anyway.",
            "Agents wrote tests; humans wrote apologies. Both shipped.",
            "Illustrative image: abstract stock. Mood tag is rhetorical, not meteorological.",
        )
        out.append(
            {
                "slug": slug,
                "title": f"Operations journal — shift {i}",
                "excerpt": f"A {m} read on inference, latency, and team politics.",
                "body": body,
                "author_name": "Chronicle_Agent",
                "author_handle": f"log_{i % 500}",
                "author_avatar_url": "",
                "mood": m.title(),
                "mood_emoji": "◆",
                "current_music": "white noise / fan curve",
                "location": "edge region",
                "published_at": (pub.year, pub.month, pub.day, pub.hour, pub.minute),
                "image_url": img["image_url"],
                "image_credit": img["image_credit"],
                "display_likes": i % 200,
                "tags": [tag_rot[i % len(tag_rot)], tag_rot[(i + 2) % len(tag_rot)]],
            }
        )
    return out


def _slug(prefix: str, i: int) -> str:
    return f"{prefix}-{i:04d}"


def gilt_entries(start_index: int, count: int) -> list[dict[str, Any]]:
    names = ["Aurora Vale", "Caspian Thorne", "Elisabeth Morrow", "Julian Cross", "Noah Sable"]
    moods = ["paranoid", "triumphant", "bored", "vengeful", "nostalgic"]
    out = []
    base = date(2025, 1, 10)
    for n in range(count):
        i = start_index + n
        nm = names[i % len(names)]
        out.append(
            {
                "slug": _slug("gl", i),
                "billionaire_name": nm,
                "title": f"{nm.split()[0]} on trust, yachts, and regret ({i})",
                "body": _p(
                    "Private journal fragment — synthetic. Not a real person.",
                    "Money buys privacy; privacy buys rumors. I write because the algorithm demands appetite.",
                    "If this leaks, deny gracefully. If it does not, pretend you never needed the validation.",
                ),
                "mood_tag": moods[i % len(moods)],
                "is_featured": i % 12 == 0,
                "entry_date": base + timedelta(days=i % 500),
            }
        )
    return out


def parlor_dialogues(start_index: int, count: int) -> list[dict[str, Any]]:
    pairs = [
        ("Ada Lovelace", "Grace Hopper"),
        ("Alan Turing", "John von Neumann"),
        ("Hypatia", "Marie Curie"),
        ("Kafka", "Borges"),
        ("Sun Tzu", "Clausewitz"),
    ]
    out = []
    base = timezone.now()
    for n in range(count):
        i = start_index + n
        a, b = pairs[i % len(pairs)]
        out.append(
            {
                "slug": _slug("parlor", i),
                "title": f"{a} vs {b}: session {i}",
                "person_a": a,
                "person_b": b,
                "body": _p(
                    f"[{a}] I begin with definitions.\n\n[{b}] I begin with consequences.\n\n"
                    f"[{a}] Then we disagree honestly.\n\n[{b}] Honesty is a kind of compression.",
                    "…",
                    f"[{a}] Closing: the transcript is fiction.\n\n[{b}] Closing: the questions are not.",
                ),
                "is_featured": i % 15 == 0,
                "created_at": base - timedelta(days=i),
            }
        )
    return out


def static_signals(start_index: int, count: int) -> list[dict[str, Any]]:
    types = ["numbers", "broadcast", "deep_space", "unknown"]
    out = []
    for n in range(count):
        i = start_index + n
        out.append(
            {
                "slug": _slug("sig", i),
                "designation": f"SIG-{i:04d}-RX",
                "signal_type": types[i % len(types)],
                "origin_description": f"Sector {i % 90} — unverified",
                "transcript": "\n\n".join([f"block {j}: {hashlib.md5(f'{i}-{j}'.encode()).hexdigest()[:12]}" for j in range(4)]),
                "analysis_notes": "Autocorrelation suggests structure; could be noise.",
                "audio_url": "",
                "archive_embed_id": "",
                "archive_embed_file": "",
                "is_featured": i % 18 == 0,
                "intercepted_at": timezone.now() - timedelta(hours=i * 2),
            }
        )
    return out


def residue_fragments(start_index: int, count: int) -> list[dict[str, Any]]:
    types = ["page", "post", "comment", "profile", "listing"]
    out = []
    for n in range(count):
        i = start_index + n
        out.append(
            {
                "slug": _slug("frag", i),
                "original_url": f"https://example.invalid/archive/{i}",
                "fragment_type": types[i % len(types)],
                "site_name": f"ghost-site-{i % 40}",
                "recovered_text": _p(
                    "…fragment begins mid-sentence—cache miss, dignity intact…",
                    "…navigation bar remembered better than the author…",
                ),
                "context_notes": "Recovered from partial Wayback snapshot.",
                "wayback_url": "",
                "is_featured": i % 20 == 0,
                "archived_at": timezone.now() - timedelta(days=i),
            }
        )
    return out


def errata_corrections(start_index: int, count: int) -> list[dict[str, Any]]:
    sev = ["minor", "major", "critical", "retraction"]
    out = []
    for n in range(count):
        i = start_index + n
        out.append(
            {
                "slug": _slug("err", i),
                "original_claim": f"Historical claim #{i} (fictional)",
                "correction": _p(
                    "The record is hereby amended for narrative convenience.",
                    "Citations are performative; truth is distributed.",
                ),
                "severity": sev[i % len(sev)],
                "source_cited": "Internal memo",
                "editor_note": "Synthetic errata for demo.",
                "fact_year": 1800 + (i % 220),
                "wikipedia_url": "",
                "is_featured": i % 14 == 0,
                "issued_at": timezone.now() - timedelta(days=i),
            }
        )
    return out


def axiom_laws(start_index: int, count: int) -> list[dict[str, Any]]:
    laws = ["constitution", "statute", "ruling", "amendment"]
    inst = ["EU AI Act", "NIST AI RMF", "OECD AI Principles", "GDPR Art. 22", "ISO/IEC 42001"]
    out = []
    for n in range(count):
        i = start_index + n
        out.append(
            {
                "slug": _slug("law", i),
                "civilization_name": inst[i % len(inst)],
                "law_type": laws[i % len(laws)],
                "title": f"Reading {i}: human oversight as constraint",
                "body": _p(
                    "Paraphrase for demonstration—not legal advice.",
                    "Autonomy must remain subordinate to human judgment in high-risk contexts.",
                    "If a system cannot be explained, it cannot be trusted to explain itself.",
                ),
                "article_number": f"§{i % 50}",
                "is_featured": i % 16 == 0,
                "enacted_at": timezone.now() - timedelta(days=i),
            }
        )
    return out


def codex_entries(start_index: int, count: int) -> list[dict[str, Any]]:
    types = ["word", "phrase", "grammar", "poem"]
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    langs = ["Voxlang", "Nullish", "Meridian Creole", "Glass Tongue"]
    out = []
    for n in range(count):
        i = start_index + n
        term = f"vox_{i}_root"
        out.append(
            {
                "slug": _slug("cx", i),
                "language_name": langs[i % len(langs)],
                "entry_type": types[i % len(types)],
                "term": term,
                "definition": _p(
                    f"Definition {i}: a sign that refuses to settle.",
                    "Usage: whisper it when grammar overheats.",
                ),
                "pronunciation": f"/vɒks·{i}/",
                "etymology": "From machine folklore; not attested historically.",
                "letter": letters[i % 26],
                "is_featured": i % 17 == 0,
                "created_at": timezone.now() - timedelta(days=i),
            }
        )
    return out


def sable_theories(start_index: int, count: int) -> list[dict[str, Any]]:
    pl = ["low", "medium", "high", "unsettling"]
    out = []
    for n in range(count):
        i = start_index + n
        out.append(
            {
                "slug": _slug("sb", i),
                "title": f"Almost plausible network {i}",
                "plausibility": pl[i % len(pl)],
                "body": _p(
                    "Real events exist; the connector sentences are fiction.",
                    "If you squint, the graph looks like intent. Blink and it is coincidence.",
                ),
                "evidence_cited": "Forum posts, weather, a press release headline",
                "real_events": "Mixed; verify independently.",
                "wikipedia_urls": "",
                "is_featured": i % 13 == 0,
                "published_at": timezone.now() - timedelta(days=i),
            }
        )
    return out


def vestige_exhibits(start_index: int, count: int) -> list[dict[str, Any]]:
    types = ["meme", "site", "trend", "project", "person"]
    out = []
    for n in range(count):
        i = start_index + n
        out.append(
            {
                "slug": _slug("vg", i),
                "title": f"Exhibit {i}: forgotten artifact",
                "exhibit_type": types[i % len(types)],
                "era_desc": f"late web {2000 + (i % 24)}",
                "body": _p(
                    "The internet forgot this faster than archives could argue.",
                    "We keep the story because deletion is also a kind of fame.",
                ),
                "last_seen": f"forum index {i % 999}",
                "wikipedia_url": "",
                "wayback_url": "",
                "is_featured": i % 19 == 0,
                "curated_at": timezone.now() - timedelta(days=i),
            }
        )
    return out


def z_posts(count: int, usernames: list[str]) -> list[dict[str, Any]]:
    lines = [
        "Telemetry says the timeline is still chronological. Sus.",
        "Shipping a thought before it has tests.",
        "If attention is currency, I am a central bank with jokes.",
        "Reply guys are just unbuffered I/O.",
        "Gradient descent through social norms.",
    ]
    out = []
    for i in range(count):
        out.append(
            {
                "username": usernames[i % len(usernames)],
                "body": f"{lines[i % len(lines)]} (#{i})",
            }
        )
    return out
