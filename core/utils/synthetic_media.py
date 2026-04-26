"""
Local synthetic images for article seeds: bundled PNGs, optional SD sidecar, else Pillow.

Paths are under ``MEDIA_ROOT/synthetic/...``; public URLs stored in the DB are **same-origin**
path URLs under ``MEDIA_URL`` (e.g. ``/media/synthetic/verso/foo.png?v=…``) so they match the
page origin (avoids ``localhost`` vs ``127.0.0.1`` mismatches and stays within CSP ``img-src 'self'``).

**Batch / offline quality:** pre-rendered files under ``assets/seed_heroes/{verso|khula|chronicle|z}/`` are
copied in at seed time when :envvar:`SYNTHETIC_MODE` is ``auto`` (default) or ``offline`` — no inference
for those slugs. See :file:`assets/seed_heroes/README.md` and :envvar:`SEED_HEROES_DIR`.

When :envvar:`SEED_IMAGE_GROUNDED` is true (default), SD/Pillow prompts include a **sanitized** snippet
from title/excerpt (trademark tokens stripped). See ``docs/AGENT_CONTENT_RULES.md``.
"""

from __future__ import annotations

import hashlib
import os
import random
import re
import shutil
from io import BytesIO
from typing import Any

import requests
from django.conf import settings
from PIL import Image, ImageDraw, ImageFilter

# Khula hand-seed articles: prefix kept for editorial honesty (was apply_khula_curated_heroes).
KHULA_CURATED_EXCERPT_PREFIX = (
    "Illustrative stock photo—not from the collection or runway named below. "
)
KHULA_CURATED_SLUGS: frozenset[str] = frozenset(
    {
        "rick-owens-hostile-comfort",
        "comme-refusal-of-legibility",
        "margiela-tabi-interface",
        "undercover-jun-takahashi-punk-poetry",
        "haider-ackermann-silk-funeral",
        "ann-demeulemeester-ink-and-ghost",
        "entropy-of-balance-berg-knutsson",
        "lvmh-is-a-moodboard",
        "algorithmic-drape-simulation",
        "schiaparelli-surrealism-as-software",
        "atelier-404-the-beautiful-mistake",
        "dries-van-noten-color-as-revenge",
        "japanese-denim-myth-of-slow",
        "deadstock-silk-luxury-beautiful-lie",
        "lagos-not-waiting-for-paris",
        "tbilisi-problem-scene-outgrows-city",
        "bottega-veneta-after-the-hype",
        "yohji-yamamoto-last-romantic",
        "fast-fashion-not-the-enemy",
        "invisible-seam-hand-thinking",
    }
)

# Single-token strip list for image prompts (fashion / luxury names; not exhaustive; geography kept).
_TRADEMARK_TOKENS: frozenset[str] = frozenset(
    {
        "prada", "chanel", "dior", "gucci", "louis", "vuitton", "balenciaga", "fendi", "versace",
        "burberry", "givenchy", "laurent", "céline", "celine", "loewe", "bottega", "veneta", "sander",
        "maison", "margiela", "owens", "kawakubo", "comme", "garçons", "garcons", "dries", "noten",
        "schiaparelli", "jil", "sacai", "lemaire", "acne", "mugler", "lvmh", "hermès", "hermes", "miyake",
        "yohji", "yamamoto", "gaultier",         "undercover", "takahashi", "demeulemeester", "ackermann", "knutsson",
        "schiap", "yohji", "rick", "saint", "rolex", "zara", "shein", "ssense",
    }
)

_BASE_PALETTE_COLORS: tuple[tuple[int, int, int], ...] = (
    (20, 24, 40), (32, 40, 64), (48, 36, 52), (24, 48, 44), (40, 32, 28), (52, 44, 48),
    (18, 22, 32), (30, 28, 36), (25, 30, 45), (28, 32, 40), (45, 40, 55), (50, 55, 65),
    (35, 45, 50), (36, 36, 44), (32, 40, 38), (15, 28, 42), (42, 36, 50),
)


def _grounded_enabled() -> bool:
    return _bool_env("SEED_IMAGE_GROUNDED", default=True)


def _max_prompt_words() -> int:
    try:
        return max(4, int(os.environ.get("SEED_IMAGE_MAX_PROMPT_WORDS", "40")))
    except ValueError:
        return 40


def _default_negative_sd() -> str:
    return os.environ.get(
        "SD_DEFAULT_NEGATIVE_PROMPT",
        "text, watermark, signature, logo, deformed, blurry, low quality, ugly, bad anatomy, "
        "extra limbs, word, writing, label",
    )


def _strip_for_prompt(s: str) -> str:
    s = re.sub(r"[*_`#]+", " ", s)
    s = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _topic_snippet(
    title: str = "",
    excerpt: str = "",
    *,
    strip_khula_prefix: bool = False,
) -> str:
    if not _grounded_enabled():
        return ""
    t = _strip_for_prompt((title or "").strip())[:300]
    e = (excerpt or "").strip()
    if strip_khula_prefix and e.startswith(KHULA_CURATED_EXCERPT_PREFIX):
        e = e[len(KHULA_CURATED_EXCERPT_PREFIX) :]
    e = _strip_for_prompt(e)[:200]
    raw = f"{t} {e}".strip()[:500]
    if not raw:
        return ""
    out: list[str] = []
    for w in re.split(r"\s+", raw):
        w2 = w.strip(".,;:!?\"'()")
        w_clean = w2.lower()
        if not w2 or w_clean in _TRADEMARK_TOKENS:
            continue
        if len(w_clean) < 2:
            continue
        out.append(w2)
        if len(out) >= _max_prompt_words():
            break
    return " ".join(out).strip()


def _diversity_key(slug: str, snippet: str) -> str:
    return f"{slug}|{snippet}" if snippet else slug


def _procedural_palette_from_key(diversity_key: str) -> tuple[tuple[int, int, int], ...]:
    h = int(hashlib.sha256(diversity_key.encode("utf-8")).hexdigest()[:12], 16)
    rng = random.Random(h)
    k = min(4, len(_BASE_PALETTE_COLORS))
    return tuple(rng.sample(_BASE_PALETTE_COLORS, k=k))


def _procedural_line_params(diversity_key: str) -> tuple[int, int, float]:
    h = int(hashlib.sha256(diversity_key.encode("utf-8")).hexdigest(), 16)
    rng = random.Random(h)
    n = 8 + (h % 28)
    line_w_max = 2 + (h % 4)
    blur = 0.3 + (h % 100) / 200.0
    return n, line_w_max, min(blur, 1.2)


def _bool_env(name: str, default: bool = False) -> bool:
    v = os.environ.get(name, "")
    if not v:
        return default
    return v.lower() in ("1", "true", "yes", "on")


def _sd_enabled() -> bool:
    return _bool_env("SD_ENABLED", default=False) and bool(
        (os.environ.get("SD_URL") or "").strip()
    )


# auto: use bundled file if present, else SD, else Pillow. offline: bundled only (missing → error).
# generate: always SD (if enabled) or Pillow, ignore bundle (for refreshing assets before export).
def _synthetic_mode() -> str:
    m = (os.environ.get("SYNTHETIC_MODE", "auto") or "auto").strip().lower()
    if m in ("auto", "offline", "generate"):
        return m
    return "auto"


def _try_bundled_png(subdir: str, filename: str) -> tuple[str, str] | None:
    if _synthetic_mode() == "generate":
        return None
    src: Any = settings.SEED_HEROES_DIR / subdir / filename
    if not src.is_file():
        return None
    media_root: Any = settings.MEDIA_ROOT
    out_dir = media_root / "synthetic" / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / filename
    shutil.copy2(src, dest)
    rel = f"synthetic/{subdir}/{filename}"
    v = hashlib.sha256(dest.read_bytes()).hexdigest()[:10]
    credit = os.environ.get(
        "SEED_HERO_OFFLINE_CREDIT",
        "Pre-rendered seed image (bundled in repository).",
    )
    return public_url_for_path(rel, cache_bust=v), credit


def _require_offline_or_continue(subdir: str, filename: str) -> None:
    if _synthetic_mode() != "offline":
        return
    raise FileNotFoundError(
        f"Offline mode (SYNTHETIC_MODE=offline): missing bundled asset. "
        f"Expected: {settings.SEED_HEROES_DIR / subdir / filename!s}"
    )


def _stable_int(*parts: str) -> int:
    h = hashlib.sha256("|".join(parts).encode("utf-8")).digest()
    return int.from_bytes(h[:4], "big") % (2**31 - 1)


def public_url_for_path(
    relative_under_media: str, *, cache_bust: str | None = None
) -> str:
    """Path under the site, e.g. ``/media/synthetic/verso/foo.png`` (and optional ``?v=``).

    ``relative_under_media`` is the path *inside* media root, e.g. ``synthetic/verso/foo.png``.
    """
    media = (getattr(settings, "MEDIA_URL", "/media/") or "/media/").strip()
    if not media.startswith("/"):
        media = "/" + media.lstrip("/")
    base = media.rstrip("/")
    rel = relative_under_media.lstrip("/")
    out = f"{base}/{rel}" if rel else f"{base}/"
    if cache_bust:
        sep = "&" if "?" in out else "?"
        out = f"{out}{sep}v={cache_bust}"
    return out


def _save_png_bytes(subdir: str, filename: str, data: bytes) -> tuple[str, str]:
    media_root: Any = settings.MEDIA_ROOT
    out_dir = media_root / "synthetic" / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    path.write_bytes(data)
    rel = f"synthetic/{subdir}/{filename}"
    v = hashlib.sha256(data).hexdigest()[:10]
    return public_url_for_path(rel, cache_bust=v), rel


def _procedural_png(
    *,
    subdir: str,
    name: str,
    width: int,
    height: int,
    seed: int,
    diversity_key: str,
) -> tuple[str, str]:
    """Fallback art: varied palette and stroke density from ``diversity_key`` (e.g. slug + topic snippet)."""
    palette = _procedural_palette_from_key(diversity_key)
    n_line, w_max, blur_r = _procedural_line_params(diversity_key)
    rng = random.Random(seed)
    base = Image.new("RGB", (width, height), palette[rng.randrange(len(palette))])
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for _ in range(n_line):
        x0, y0 = rng.randint(0, width), rng.randint(0, height)
        x1, y1 = rng.randint(0, width), rng.randint(0, height)
        c = (*rng.sample(range(80, 256), 3), rng.randint(20, 90))
        draw.line((x0, y0, x1, y1), fill=c, width=rng.randint(1, w_max))
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, overlay)
    base_rgb = base_rgba.convert("RGB")
    base_rgb = base_rgb.filter(ImageFilter.GaussianBlur(radius=blur_r))
    buf = BytesIO()
    base_rgb.save(buf, format="PNG", optimize=True)
    data = buf.getvalue()
    credit = f"Synthetic image (Pillow, seed={seed})"
    url, _rel = _save_png_bytes(subdir, f"{name}.png", data)
    return url, credit


def _try_sd_image(
    prompt: str,
    *,
    seed: int,
    width: int,
    height: int,
    subdir: str,
    name: str,
    negative_prompt: str | None = None,
) -> tuple[str, str] | None:
    if not _sd_enabled():
        return None
    url = (os.environ.get("SD_URL") or "").strip().rstrip("/")
    if not url:
        return None
    timeout = int(os.environ.get("SD_TIMEOUT_SECONDS", "300"))
    neg = negative_prompt if negative_prompt is not None else _default_negative_sd()
    payload: dict[str, Any] = {
        "prompt": prompt,
        "negative_prompt": neg,
        "seed": seed,
        "width": width,
        "height": height,
    }
    try:
        r = requests.post(f"{url}/generate", json=payload, timeout=timeout)
        r.raise_for_status()
        data = r.content
        if not data or len(data) < 32:
            return None
        u, _ = _save_png_bytes(subdir, f"{name}.png", data)
        return u, f"Synthetic image (local SD, seed={seed})"
    except (OSError, requests.RequestException, ValueError):
        return None


def _verso_sd_prompt(category: str, topic_snippet: str) -> str:
    if _grounded_enabled() and topic_snippet:
        return (
            f"Cinematic wide editorial still, {category} technology and ideas, "
            f"visual themes: {topic_snippet}, professional lighting, depth, mood, "
            f"no text, no logos, no people, no readable characters, 8k, highly detailed"
        )
    return (
        f"Cinematic wide editorial still, {category} technology, moody professional lighting, "
        f"depth, atmosphere, no text, no logos, no people, 8k, detailed"
    )


def _khula_sd_prompt(category: str, topic_snippet: str) -> str:
    if _grounded_enabled() and topic_snippet:
        return (
            f"Editorial high fashion still life and fabric study, {category} sensibility, "
            f"visual themes: {topic_snippet}, soft studio light, drape and texture, "
            f"no text, no logos, no people, no mannequins, 8k, detailed, moody"
        )
    return (
        f"Editorial fashion still life, {category} mood, fabric drape, studio light, "
        f"no text, no logos, no people, 8k, detailed"
    )


def _chronicle_hero_sd_prompt(primary_tag: str, topic_snippet: str) -> str:
    if _grounded_enabled() and topic_snippet:
        return (
            f"Cinematic editorial photograph, {primary_tag} systems and operations, "
            f"visual themes: {topic_snippet}, server room haze, glass and light, cool tones, "
            f"no text, no logos, no people, no UI text, 8k, detail"
        )
    return (
        f"Cinematic editorial, {primary_tag} technology infrastructure, cool tones, "
        f"glass and light, no text, no logos, no people, 8k, detail"
    )


def _chronicle_avatar_sd_prompt(handle: str, title_hint: str) -> str:
    if _grounded_enabled() and title_hint:
        return (
            f"Abstract minimal square brand avatar, color fields suggestive of: {title_hint[:80]}, "
            f"no face, no text, no logos, clean modern"
        )
    return (
        "Minimal abstract square avatar, soft color blocks, no face, no text, no logos, clean"
    )


def _z_sd_prompt(topic_snippet: str) -> str:
    if _grounded_enabled() and topic_snippet:
        return (
            f"Wide social network banner, editorial mood, themes: {topic_snippet}, "
            f"no text, no faces, no logos, clean composition, 8k"
        )
    return (
        "Wide editorial banner, soft abstract gradient, no text, no faces, no logos, 8k"
    )


def generate_verso_hero(
    slug: str,
    *,
    category: str,
    title: str = "",
    excerpt: str = "",
) -> tuple[str, str]:
    seed = _stable_int("verso", slug, "hero")
    w, h = 1024, 576
    name = f"verso-{_slugify(slug)}"
    fn = f"{name}.png"
    b = _try_bundled_png("verso", fn)
    if b is not None:
        return b
    _require_offline_or_continue("verso", fn)
    snippet = _topic_snippet(title, excerpt, strip_khula_prefix=False)
    p = _verso_sd_prompt(category, snippet)
    dkey = _diversity_key(slug, snippet)
    out = _try_sd_image(p, seed=seed, width=w, height=h, subdir="verso", name=name)
    if out:
        return out
    return _procedural_png(
        subdir="verso", name=name, width=w, height=h, seed=seed, diversity_key=dkey,
    )


def generate_khula_hero(
    slug: str,
    *,
    category: str,
    title: str = "",
    excerpt: str = "",
) -> tuple[str, str]:
    seed = _stable_int("khula", slug, "hero")
    w, h = 1024, 576
    name = f"khula-{_slugify(slug)}"
    fn = f"{name}.png"
    b = _try_bundled_png("khula", fn)
    if b is not None:
        return b
    _require_offline_or_continue("khula", fn)
    snippet = _topic_snippet(title, excerpt, strip_khula_prefix=True)
    p = _khula_sd_prompt(category, snippet)
    dkey = _diversity_key(slug, snippet)
    out = _try_sd_image(p, seed=seed, width=w, height=h, subdir="khula", name=name)
    if out:
        return out
    return _procedural_png(
        subdir="khula", name=name, width=w, height=h, seed=seed, diversity_key=dkey,
    )


def generate_chronicle_hero(
    slug: str,
    *,
    primary_tag: str,
    title: str = "",
    excerpt: str = "",
) -> tuple[str, str]:
    seed = _stable_int("chronicle", slug, "hero")
    w, h = 1024, 576
    name = f"chronicle-hero-{_slugify(slug)}"
    fn = f"{name}.png"
    b = _try_bundled_png("chronicle", fn)
    if b is not None:
        return b
    _require_offline_or_continue("chronicle", fn)
    snippet = _topic_snippet(title, excerpt, strip_khula_prefix=False)
    p = _chronicle_hero_sd_prompt(primary_tag, snippet)
    dkey = _diversity_key(slug, snippet)
    out = _try_sd_image(p, seed=seed, width=w, height=h, subdir="chronicle", name=name)
    if out:
        return out
    return _procedural_png(
        subdir="chronicle", name=name, width=w, height=h, seed=seed, diversity_key=dkey,
    )


def generate_chronicle_avatar(
    handle: str,
    *,
    entry_title: str = "",
) -> tuple[str, str]:
    seed = _stable_int("chronicle", "avatar", handle)
    w = h = 256
    name = f"chronicle-av-{_slugify(handle)}"
    fn = f"{name}.png"
    b = _try_bundled_png("chronicle", fn)
    if b is not None:
        return b
    _require_offline_or_continue("chronicle", fn)
    hint = _topic_snippet(entry_title, "", strip_khula_prefix=False) if _grounded_enabled() else ""
    p = _chronicle_avatar_sd_prompt(handle, hint)
    dkey = _diversity_key(handle, hint)
    out = _try_sd_image(p, seed=seed, width=w, height=h, subdir="chronicle", name=name)
    if out:
        return out
    return _procedural_png(
        subdir="chronicle", name=name, width=w, height=h, seed=seed, diversity_key=dkey,
    )


def generate_z_post_media(suffix: str, body: str = "") -> tuple[str, str]:
    seed = _stable_int("z", "post", suffix)
    w, h = 800, 400
    name = f"z-{_slugify(suffix)}"
    fn = f"{name}.png"
    b = _try_bundled_png("z", fn)
    if b is not None:
        return b
    _require_offline_or_continue("z", fn)
    snippet = _topic_snippet("", body[:500], strip_khula_prefix=False) if body else ""
    p = _z_sd_prompt(snippet)
    dkey = _diversity_key(suffix, snippet)
    out = _try_sd_image(p, seed=seed, width=w, height=h, subdir="z", name=name)
    if out:
        return out
    return _procedural_png(
        subdir="z", name=name, width=w, height=h, seed=seed, diversity_key=dkey,
    )


def _slugify(s: str) -> str:
    out = []
    for ch in s.lower():
        if ch.isalnum():
            out.append(ch)
        else:
            out.append("-")
    x = "".join(out)
    while "--" in x:
        x = x.replace("--", "-")
    return x.strip("-") or "x"


def ensure_khula_excerpt_honesty(articles: list[dict[str, Any]]) -> None:
    for art in articles:
        slug = art.get("slug", "")
        if slug not in KHULA_CURATED_SLUGS:
            continue
        excerpt = art.get("excerpt") or ""
        if KHULA_CURATED_EXCERPT_PREFIX not in excerpt:
            art["excerpt"] = KHULA_CURATED_EXCERPT_PREFIX + excerpt
