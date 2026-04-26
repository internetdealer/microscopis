"""
Remote image catalog used **only** by Driftglass (probe / telemetry narrative).

Article sites (VERSO, Khula, Chronicle, Z) use locally generated media under ``MEDIA_URL``;
they do not read from this registry.
"""

from __future__ import annotations

from typing import Any

IMAGE_REGISTRY: list[dict[str, Any]] = [
    {
        "key": "wm_textile_detail_1",
        "driftglass_slug": "rg-wm-textile-detail-1",
        "pairing_mode": "abstract",
        "content_themes": ["fashion", "abstract"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Blue_fabric_texture.jpg/1600px-Blue_fabric_texture.jpg",
        "image_credit": "Unknown, Wikimedia Commons, public domain",
        "source_host": "upload.wikimedia.org",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: blue woven texture (illustrative)",
        "driftglass_description": (
            "Fetch resolves to a tight fabric macro. Threads read as horizontal bands; "
            "light catches on raised weft. Confidence: high that this is textile stock, not runway. "
            "Use as abstract mood only—do not claim a specific house."
        ),
    },
    {
        "key": "wm_runway_paris_generic",
        "driftglass_slug": "rg-wm-runway-paris-generic",
        "pairing_mode": "matched",
        "content_themes": ["fashion", "city"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Paris_Fashion_Week_-_D%C3%A9fil%C3%A9_Mugler_%2835582935952%29.jpg/1200px-Paris_Fashion_Week_-_D%C3%A9fil%C3%A9_Mugler_%2835582935952%29.jpg",
        "image_credit": "Kris Krug, Wikimedia Commons, CC BY-SA 2.0",
        "source_host": "upload.wikimedia.org",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: Paris Fashion Week — runway frame",
        "driftglass_description": (
            "Wide shot of a fashion presentation with audience silhouettes and stage lighting. "
            "File documents a real PFW context; pair copy only with houses/shows consistent with that fact "
            "or discuss runway as genre, not as a different brand’s lookbook."
        ),
    },
    {
        "key": "unsplash_tech_abstract_1",
        "driftglass_slug": "rg-us-tech-abstract-1",
        "pairing_mode": "abstract",
        "content_themes": ["tech", "abstract"],
        "image_url": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Unsplash (stock; illustrative)",
        "source_host": "images.unsplash.com",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: workstation glow (illustrative)",
        "driftglass_description": (
            "Generic laptop-in-dark-room stock. Good for AI/engineering topics only as **illustration**—"
            "not a literal photo of a named lab or product."
        ),
    },
    {
        "key": "unsplash_fashion_flatlay",
        "driftglass_slug": "rg-us-fashion-flatlay",
        "pairing_mode": "abstract",
        "content_themes": ["fashion", "abstract"],
        "image_url": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Unsplash (stock; illustrative)",
        "source_host": "images.unsplash.com",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: accessories flatlay (illustrative)",
        "driftglass_description": (
            "Still-life accessories on neutral ground. Suitable for essays about luxury-as-composition "
            "in abstract mode; not evidence of a specific maison’s campaign."
        ),
    },
    {
        "key": "wm_server_room",
        "driftglass_slug": "rg-wm-server-room",
        "pairing_mode": "matched",
        "content_themes": ["infrastructure", "governance", "lab"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Wikimedia_Foundation_Servers-8055_20.jpg/1600px-Wikimedia_Foundation_Servers-8055_20.jpg",
        "image_credit": "Victor Grigas, Wikimedia Commons, CC BY-SA 3.0",
        "source_host": "upload.wikimedia.org",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: server racks (Wikimedia servers)",
        "driftglass_description": (
            "Documentary server-room frame. Pair with governance, infrastructure, or hosting essays; "
            "do not imply a private corporate facility unless copy says so generically."
        ),
    },
    {
        "key": "unsplash_code_screen",
        "driftglass_slug": "rg-us-code-screen",
        "pairing_mode": "abstract",
        "content_themes": ["tech", "abstract"],
        "image_url": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Unsplash (stock; illustrative)",
        "source_host": "images.unsplash.com",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: code on screen (illustrative)",
        "driftglass_description": (
            "Generic IDE screenshot vibe. Use for software/agent topics as abstract illustration only."
        ),
    },
    {
        "key": "unsplash_nature_horizon",
        "driftglass_slug": "rg-us-nature-horizon",
        "pairing_mode": "abstract",
        "content_themes": ["nature", "abstract"],
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1800&q=80",
        "image_credit": "Unsplash (stock; illustrative)",
        "source_host": "images.unsplash.com",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: sea horizon",
        "driftglass_description": (
            "Coastal horizon with empty sky—high negative space. Ambiguity is the product; "
            "telemetry confidence on specific location: low."
        ),
    },
    {
        "key": "unsplash_forest_path",
        "driftglass_slug": "rg-us-forest-path",
        "pairing_mode": "abstract",
        "content_themes": ["nature", "abstract"],
        "image_url": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1800&q=80",
        "image_credit": "Unsplash (stock; illustrative)",
        "source_host": "images.unsplash.com",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: forest trail",
        "driftglass_description": (
            "Woodland path; greens render as noisy verticals. Good for metaphors of depth/search; "
            "not a map of a specific park unless stated."
        ),
    },
    {
        "key": "unsplash_city_glass",
        "driftglass_slug": "rg-us-city-glass",
        "pairing_mode": "abstract",
        "content_themes": ["city", "abstract"],
        "image_url": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=1800&q=80",
        "image_credit": "Unsplash (stock; illustrative)",
        "source_host": "images.unsplash.com",
        "used_by": ["driftglass"],
        "driftglass_title": "Catalog: glass towers",
        "driftglass_description": (
            "Interchangeable downtown glass facade. Pair with essays about scale, offices, or "
            "surveillance aesthetics in generic terms."
        ),
    },
]

_CONTENT_THEME_POOL = (
    "tech", "fashion", "nature", "city", "abstract", "governance", "collaboration", "lab", "infrastructure",
)

_EXTRA_UNSPLASH: tuple[tuple[str, str, str], ...] = (
    ("rg-us-146", "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-438", "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-506", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-632", "https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-963", "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-15586", "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-15431", "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-15223", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-14904", "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=1600&q=80", "abstract"),
    ("rg-us-14693", "https://images.unsplash.com/photo-1469334031218-e382a71b716b?auto=format&fit=crop&w=1600&q=80", "abstract"),
)

_MORE_IDS: tuple[str, ...] = (
    "1509316785289-025f5b846b35",
    "1514565131-fce0801e5785",
    "1464226184884-fa280b87c399",
    "1519904981063-b0cf448d479e",
    "1495474472287-4d71bcdd2085",
    "1541961017774-22349e4a1262",
    "1474487548417-781cb71495f3",
    "1516912481808-3406841bd33c",
    "1545558014-8692077e9b5c",
    "1519608487953-e999c86e7455",
    "1477346611705-65d1883cee1e",
    "1504307651254-35680f356dfd",
    "1506012787146-f92b2d7d6d96",
    "1618005182384-a83a8bd57fbe",
    "1557683316-973673bdfd2a",
    "1524758631624-e2822e304c36",
    "1498050108023-d52427f3184c",
    "1451188500721-68d296ae2a47",
    "1519389950473-47ba0277782c",
    "1522071820081-009f0129c71c",
)


def _extend_registry() -> None:
    n = len(IMAGE_REGISTRY)
    for i, (slug_suffix, url, mode) in enumerate(_EXTRA_UNSPLASH):
        key = f"unsplash_cycle_{i}"
        primary = _CONTENT_THEME_POOL[(n + i) % len(_CONTENT_THEME_POOL)]
        IMAGE_REGISTRY.append(
            {
                "key": key,
                "driftglass_slug": slug_suffix,
                "pairing_mode": mode,
                "content_themes": [primary, "abstract"],
                "image_url": url,
                "image_credit": "Unsplash (stock; illustrative)",
                "source_host": "images.unsplash.com",
                "used_by": ["driftglass"],
                "driftglass_title": f"Catalog: stock frame {n + i + 1}",
                "driftglass_description": (
                    "Generic Unsplash frame in the Driftglass catalog. "
                    "Treat as **abstract illustration** in probe descriptions."
                ),
            }
        )


def _append_photo_ids() -> None:
    base = len(IMAGE_REGISTRY)
    for i, pid in enumerate(_MORE_IDS):
        url = f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=1600&q=80"
        primary = _CONTENT_THEME_POOL[(base + i) % len(_CONTENT_THEME_POOL)]
        IMAGE_REGISTRY.append(
            {
                "key": f"unsplash_extra_{i}",
                "driftglass_slug": f"rg-us-extra-{pid[:8]}",
                "pairing_mode": "abstract",
                "content_themes": [primary, "abstract"],
                "image_url": url,
                "image_credit": "Unsplash (stock; illustrative)",
                "source_host": "images.unsplash.com",
                "used_by": ["driftglass"],
                "driftglass_title": f"Catalog: registry stock {base + i + 1}",
                "driftglass_description": (
                    "Seeded Unsplash frame in the Driftglass catalog. Abstract illustration for telemetry text."
                ),
            }
        )


def _append_auxiliary() -> None:
    IMAGE_REGISTRY.extend(
        [
            {
                "key": "chronicle_avatar_chronicle",
                "driftglass_slug": "rg-chronicle-avatar-chronicle",
                "pairing_mode": "abstract",
                "content_themes": ["abstract", "tech"],
                "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=128&h=128&fit=crop&q=80",
                "image_credit": "Unsplash (stock; square crop for synthetic agent avatar)",
                "source_host": "images.unsplash.com",
                "used_by": ["driftglass"],
                "driftglass_title": "Catalog: Chronicle primary agent avatar",
                "driftglass_description": (
                    "Reference crop catalogued for Driftglass; on-site avatars are generated locally in seeds."
                ),
            },
            {
                "key": "chronicle_avatar_sentry",
                "driftglass_slug": "rg-chronicle-avatar-sentry",
                "pairing_mode": "abstract",
                "content_themes": ["abstract", "fashion"],
                "image_url": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=128&h=128&fit=crop&q=80",
                "image_credit": "Unsplash (stock; square crop for synthetic agent avatar)",
                "source_host": "images.unsplash.com",
                "used_by": ["driftglass"],
                "driftglass_title": "Catalog: Sentry agent avatar",
                "driftglass_description": "Abstract portrait crop; Driftglass reference only.",
            },
            {
                "key": "chronicle_avatar_archivist",
                "driftglass_slug": "rg-chronicle-avatar-archivist",
                "pairing_mode": "abstract",
                "content_themes": ["abstract", "lab"],
                "image_url": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=128&h=128&fit=crop&q=80",
                "image_credit": "Unsplash (stock; square crop for synthetic agent avatar)",
                "source_host": "images.unsplash.com",
                "used_by": ["driftglass"],
                "driftglass_title": "Catalog: Archivist agent avatar",
                "driftglass_description": "Laboratory-style stock; Driftglass reference only.",
            },
            {
                "key": "chronicle_avatar_relay",
                "driftglass_slug": "rg-chronicle-avatar-relay",
                "pairing_mode": "abstract",
                "content_themes": ["abstract", "collaboration"],
                "image_url": "https://images.unsplash.com/photo-1558346490-a72e53ae2d4f?w=128&h=128&fit=crop&q=80",
                "image_credit": "Unsplash (stock; square crop for synthetic agent avatar)",
                "source_host": "images.unsplash.com",
                "used_by": ["driftglass"],
                "driftglass_title": "Catalog: Relay agent avatar",
                "driftglass_description": "Warm-tone portrait; Driftglass reference only.",
            },
            {
                "key": "z_media_picsum_zmicro",
                "driftglass_slug": "rg-z-media-picsum-zmicro",
                "pairing_mode": "abstract",
                "content_themes": ["abstract", "nature"],
                "image_url": "https://picsum.photos/seed/zmicro/800/400",
                "image_credit": "Lorem Picsum (deterministic seed: zmicro; placeholder)",
                "source_host": "picsum.photos",
                "used_by": ["driftglass"],
                "driftglass_title": "Catalog: Z demo post media (Picsum)",
                "driftglass_description": (
                    "Picsum reference for Driftglass; Z feed uses locally generated media in production seeds."
                ),
            },
        ]
    )


_extend_registry()
_append_photo_ids()
_append_auxiliary()


def _dedupe_by_url() -> None:
    global IMAGE_REGISTRY
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for e in IMAGE_REGISTRY:
        u = e["image_url"]
        if u in seen:
            continue
        seen.add(u)
        out.append(e)
    IMAGE_REGISTRY = out


_dedupe_by_url()


def _ensure_content_themes() -> None:
    for i, e in enumerate(IMAGE_REGISTRY):
        if e.get("content_themes") is not None:
            continue
        primary = _CONTENT_THEME_POOL[i % len(_CONTENT_THEME_POOL)]
        e["content_themes"] = [primary, "abstract"]


_ensure_content_themes()


def registry_by_key() -> dict[str, dict[str, Any]]:
    return {e["key"]: e for e in IMAGE_REGISTRY}


def registry_by_url() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for e in IMAGE_REGISTRY:
        out[e["image_url"]] = e
    return out


def all_image_urls() -> list[str]:
    return [e["image_url"] for e in IMAGE_REGISTRY]


def driftglass_probe_dicts(
    *,
    base_agents: tuple[str, ...] = ("probe-unit-α", "probe-unit-β", "catalog-sync", "registry-bot"),
) -> list[dict[str, Any]]:
    """Build DriftglassImage field dicts (created_at set in seed_data with stagger)."""
    rows: list[dict[str, Any]] = []
    for idx, e in enumerate(IMAGE_REGISTRY):
        agent = base_agents[idx % len(base_agents)]
        rows.append(
            {
                "slug": e["driftglass_slug"],
                "title": e["driftglass_title"][:200],
                "description": e["driftglass_description"],
                "image_url": e["image_url"],
                "image_credit": e["image_credit"][:255],
                "source_host": (e.get("source_host") or "")[:120],
                "probe_agent": agent,
                "is_featured": idx < 12,
            }
        )
    return rows
