# Pre-rendered seed heroes (optional)

Drop **PNGs here** (or use `export_synthetic_bundles` after generating locally) so `seed_verso`, `seed_khula`, `seed_chronicle`, and `seed_z` can **copy** them into `MEDIA_ROOT` at seed time with **no** Stable Diffusion or Pillow inference for those files.

## Layout and filenames (must match exactly)

| Subfolder    | File name pattern (examples) |
|-------------|------------------------------|
| `verso/`    | `verso-{slugified-article-slug}.png` e.g. `verso-the-agentic-turn.png` |
| `khula/`    | `khula-{slug}.png` e.g. `khula-rick-owens-hostile-comfort.png` |
| `chronicle/`| `chronicle-hero-{slug}.png` and `chronicle-av-{author_handle}.png` |
| `z/`        | `z-{suffix}.png` e.g. `z-fixed-3.png`, `z-bulk-10.png` |

Slugs are lowercased; non-alphanumeric characters become hyphens (see `core.utils.synthetic_media._slugify`).

## Workflow

1. On a **capable** machine, set `SYNTHETIC_MODE=generate` (ignore this folder), enable SD if you want, and run the relevant `seed_*` (or the full `seed_microscopis`) so `media/synthetic/...` fills with the images you like.
2. Run **`python manage.py export_synthetic_bundles`** to copy `media/synthetic/*` into `assets/seed_heroes/`.
3. Commit the PNGs. For a large set, use **[Git LFS](https://git-lfs.com/)** (e.g. `git lfs track "assets/seed_heroes/**/*.png"`).
4. In production/CI, set **`SYNTHETIC_MODE=offline`** to require only bundled files (fails if any file is missing), or leave **`SYNTHETIC_MODE=auto`** (default) to use a bundle when present and fall back to SD/Pillow otherwise.

## Environment

- `SEED_HEROES_DIR` — override path to this bundle (default: `assets/seed_heroes` under the project root).
- `SYNTHETIC_MODE` — `auto` | `offline` | `generate` (see `core/utils/synthetic_media.py` docstring).
- `SEED_HERO_OFFLINE_CREDIT` — credit string stored in the DB for bundled images (optional).
- `SEED_IMAGE_GROUNDED` — when generating into this folder with `export_synthetic_bundles`, set `1` (default) so local SD uses title/excerpt-based prompts; see `docs/AGENT_CONTENT_RULES.md`.
