# Deploying microscopis

You can run **with Docker Compose** (PostgreSQL, Redis, Gunicorn, Celery worker + beat) or the **classic** way: Python venv on the server, **Gunicorn** bound to `127.0.0.1`, and **Nginx** (or Caddy) in front for TLS and reverse proxy.

## Docker Compose (full stack)

This path uses the [`Dockerfile`](Dockerfile) and [`docker-compose.yml`](docker-compose.yml): **Postgres 16**, **Redis 7** (app cache, rate limits, and Celery broker), **Gunicorn** (default 3 workers, 120s timeout; override with `GUNICORN_WORKERS` and `GUNICORN_TIMEOUT`), **Celery worker**, and **Celery beat** (hourly `sync_z_counters` for Z-site denormalized counts). No third-party sign-ups or API keys.

1. `cp .env.example .env` and set at least `DJANGO_SECRET_KEY`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS` (use your real domain in production). The example file disables HTTPS redirects and secure cookies for **plain HTTP** on `http://127.0.0.1:8000` (`DJANGO_SECURE_SSL_REDIRECT=false`, `SESSION_COOKIE_SECURE=false`, `CSRF_COOKIE_SECURE=false`, `SECURE_HSTS_SECONDS=0`). For a public site with TLS in front, turn those back on and set `CSRF_TRUSTED_ORIGINS` to `https://…` origins.
2. `docker compose up -d --build` — the `web` entrypoint runs migrations and `collectstatic` on startup; static files are served with WhiteNoise. On a **new** (empty) database, it also runs **`python manage.py seed_microscopis` once** so SearchIndex and all per-site seed content is loaded. The next time the container restarts, seeding is skipped. To start with an empty site catalog, set **`SKIP_AUTO_SEED=1`** in `.env` before the first `up` (rare). **Do not** run `seed_microscopis` manually in another shell **during** the first container start, or you used to get duplicate inserts and cancelled statements; the command now uses a **Postgres advisory lock** so a second run waits, but you can still wait for the first boot to finish before `exec` for clarity. To re-seed after data changes, run: `docker compose exec web python manage.py seed_microscopis` (this resets `WebsiteContent` and re-runs site seeds—see the command’s help).
3. Optional: `docker compose exec web python manage.py createsuperuser`

The app is published on **port 8000** by default (`http://127.0.0.1:8000`). Postgres and Redis use named volumes (`pgdata`, `redisdata`); back up the database with `pg_dump` or volume snapshots as you would for any Postgres deployment.

**Reverse proxy and TLS**

- **TLS on the host (typical VPS):** keep the default `docker compose` services and point **Nginx** or **Caddy** on the host at `http://127.0.0.1:8000` with `X-Forwarded-Proto` and friends (same as the no-Docker flow below). You can unpublish port `8000` in the compose file if the app is only reached via the host proxy.
- **HTTP/HTTPS in Compose:** `docker compose --profile with-proxy up -d` starts **Caddy** in front of the app (see [`deploy/Caddyfile`](deploy/Caddyfile): plain HTTP on port 80; edit the file for your domain and enable automatic HTTPS for public deployments).

**Celery monitoring (optional):** `docker compose --profile flower up -d` and open `http://127.0.0.1:5555` (bound to loopback; do not expose Flower to the public internet without authentication).

**Gunicorn `WORKER TIMEOUT` / “no URI read”:** the sync worker is waiting for a full HTTP line and a client (browser probe, keep-alive, or Docker Desktop) held the connection open. The Docker entrypoint sets a **120s** timeout by default (`GUNICORN_TIMEOUT`); the previous Gunicorn default of 30s was easy to hit on a quiet tab. It is usually harmless. The `/favicon.ico` **404** in logs is from the browser; add a `favicon.ico` under static files if you want to silence it.

**Homepage / `localhost` does not load, but `/health` works (curl or `127.0.0.1`):** try **`http://127.0.0.1:8000/`** in the address bar. Some systems resolve `localhost` to **IPv6** first while Gunicorn listens on **`0.0.0.0:8000` (IPv4 only)**. We do **not** add a second `--bind [::]:8000` in Docker, because on Linux that typically collides with the IPv4 any-address bind (`Address already in use`). If the site only failed after earlier HTTPS tests, the browser may have cached **HSTS**—clear it in Chrome at `chrome://net-internals/#hsts` or use a private window, and keep `SECURE_HSTS_SECONDS=0` in `.env` for plain local HTTP.

**Slowness (especially Docker on macOS):** Docker adds host→VM→container latency and I/O cost; the **first** request after a cold start is slower (Django, DB, Redis, many static files). For faster day-to-day UI work, use a **venv** and `python manage.py runserver` (SQLite) and reserve Compose for “full stack” checks. In Compose: start only the web stack (no background workers) with `docker compose up -d web db redis`—Celery/Beat are optional for clicking around. In `.env`, set **`GUNICORN_WORKER_CLASS=gthread`**, **`GUNICORN_WORKERS=1`**, and **`GUNICORN_THREADS=6`** so Gunicorn can serve several concurrent I/O waits with one process (better under slow Docker I/O). Try both **`http://127.0.0.1:8000`** and **`http://localhost:8000`**; on some Macs one path is a bit faster than the other. In **Docker Desktop → Settings → Resources**, giving the VM a bit more CPU and memory also helps.

**Process layout without Docker:** with PostgreSQL and `REDIS_URL` set, you can run the same stack using your venv: `gunicorn` (multiple workers), `celery -A microscopis worker -l info`, and `celery -A microscopis beat -l info` (with `DJANGO_SETTINGS_MODULE=microscopis.settings.production`). Use **systemd** (or a process manager) for each long-running process.

## SQLite + no Redis (simple VPS)

This stack is supported: **SQLite** on disk and **in-process cache** (no Redis). Constraints:

- Run **one Gunicorn worker** (`--workers 1`). Several workers plus SQLite will cause database lock errors and inconsistent rate limits.
- Put the SQLite file on a persistent path (e.g. next to the app: `db.sqlite3` under the project root, which is the default if you omit `DATABASE_URL`).
- Back up `db.sqlite3` with your backups; there is no separate database server.

Optional **`REDIS_URL`**: only if you move to **multiple** Gunicorn workers (then prefer PostgreSQL for the DB too).

Optional **`DATABASE_URL`**: omit for default SQLite; set to `postgresql://...` only if you use PostgreSQL (requires `psycopg` in `requirements.txt`).

## Environment variables (production)

| Variable | Required | Notes |
|----------|----------|--------|
| `DJANGO_SETTINGS_MODULE` | Yes | `microscopis.settings.production` |
| `DJANGO_SECRET_KEY` | Yes | Long random string; never commit |
| `ALLOWED_HOSTS` | Yes | Comma-separated hostnames |
| `DATABASE_URL` | No | Defaults to SQLite at `BASE_DIR/db.sqlite3` |
| `CSRF_TRUSTED_ORIGINS` | Strongly recommended | Comma-separated origins, e.g. `https://example.com` |
| `REDIS_URL` | No | Omit for single-worker + LocMem cache |
| `SECURE_HSTS_SECONDS` | Optional | Default `3600`; use `0` to disable HSTS during first TLS tests |
| `DJANGO_SECURE_SSL_REDIRECT` | Optional | Default `true`; set `false` only if TLS is terminated upstream and `X-Forwarded-Proto` is wrong |
| `DJANGO_ADMIN_URL` | Optional | Path segment for admin (default `admin`) |
| `PUBLIC_CACHE_MAX_AGE` | Optional | Seconds for `Cache-Control` on anonymous HTML (default `300`) |
| `DATABASE_CONN_MAX_AGE` | Optional | Default `0` for SQLite, `120` for other backends |
| `GUNICORN_WORKERS` | Optional | Used by the Docker web entrypoint only; default `3` |
| `GUNICORN_TIMEOUT` | Optional | Gunicorn worker request timeout in seconds; Docker entrypoint default `120` (Gunicorn’s own default is `30`) |
| `GUNICORN_WORKER_CLASS` | Optional | Default `sync`; set `gthread` in Docker (see slowness note) with `GUNICORN_THREADS` |
| `GUNICORN_THREADS` | Optional | With `gthread` only; Docker entrypoint default `6` when using `gthread` |
| `SKIP_AUTO_SEED` | Optional | Set `1` to skip auto `seed_microscopis` on first Docker boot (empty `SearchIndex` only) |
| `USE_SYNTHETIC_SEED_FALLBACK` | Optional | Default `1`: use `bulk_generators` when `IngestedArticle` has fewer than 1300 `omni` rows. Set `0` after `ingest_web_corpus` for real web-sourced text/images |
| `INGEST_OMNI_POOL` | Optional | Default `omni` — `IngestedArticle.pool` that seeds partition; must match `ingest_web_corpus` |
| `INGEST_IMAGE_ALLOW_ALL` / `INGEST_HTTP_TIMEOUT` / `INGEST_USER_AGENT` / `INGEST_IMAGE_MAX_BYTES` | Optional | Used by `ingest_web_corpus` and `core.utils.ingest_fetch` for image hotlinking and fetches (see `ingest` command help) |
| `MEDIA_URL` / `MEDIA_ROOT` | Optional | Defaults `/media/` and `BASE_DIR/media` (Docker: `/app/media` via compose) |
| `PUBLIC_BASE_URL` | Optional | No trailing slash; for tools/emails. Seeded “local” heroes are stored as same-origin paths such as `/media/synthetic/…` (not tied to this host) |
| `SERVE_MEDIA_THROUGH_DJANGO` | Optional | Set `1` in production to serve `MEDIA_ROOT` from Gunicorn; prefer Nginx `alias` in front of a big site |
| `SD_ENABLED` / `SD_URL` | Optional | When `SD_ENABLED=1` and `SD_URL` points at the `imagegen` service, seeds call HTTP `/generate`; else Pillow |
| `SEED_SOURCED_IMAGE_ALLOW_HOSTS` | Optional | Comma-separated hosts for `ingest_sourced_hero` / `sourced_image_url` downloads; default allowlist in code; use `*` to disable host check (risky) |
| `SEED_SOURCED_IMAGE_MAX_BYTES` | Optional | Max download size; default `5000000` |
| `SEED_SOURCED_IMAGE_TIMEOUT` | Optional | HTTP timeout seconds; default `60` |
| `SEED_SKIP_IMAGE_CHECK` | Deprecated | Removed from the web entrypoint; no longer used |
| `CELERY_BROKER_URL` / `CELERY_RESULT_BACKEND` | Optional | In production, default to `REDIS_URL` when it is set |
| `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB` | Docker Compose | Configure the `db` service and default `DATABASE_URL` in `docker-compose.yml` |
| `SESSION_COOKIE_SECURE` / `CSRF_COOKIE_SECURE` | Optional | Default `true`; set `false` for plain HTTP (local Docker). If unset, default is `true`. |

## Static files

After code changes that touch static assets:

```bash
export DJANGO_SETTINGS_MODULE=microscopis.settings.production
# … export SECRET_KEY, ALLOWED_HOSTS, etc. (DATABASE_URL optional for SQLite)
python manage.py collectstatic --noinput
```

Production uses **WhiteNoise** with **compressed, manifest-hashed** filenames.

## Database

```bash
python manage.py migrate --noinput
```

After migrations, **load site content and SearchIndex** (not run automatically for non-Docker deploys unless you set it up yourself):

```bash
python manage.py seed_microscopis
```

**Web-sourced full seed (optional):** `ingest_web_corpus` fetches many articles from the RSS feeds in [`config/web_ingest/feeds.yaml`](config/web_ingest/feeds.yaml) into the `IngestedArticle` table (pool `INGEST_OMNI_POOL`, default `omni`). `seed_*` then partitions that table: each of the 13 sites in `INGEST_PARTITION_SITE_ORDER` (see `settings/base.py`) takes the next 100 rows by primary key (1300+ articles required before disabling fallback). **Two-step** on a new machine: `python manage.py ingest_web_corpus` (can take a long time; uses trafilatura + httpx) then `USE_SYNTHETIC_SEED_FALLBACK=0` and `python manage.py reset_microscopis` (or `seed_microscopis`). With **`USE_SYNTHETIC_SEED_FALLBACK=1`** (default in settings), an empty or small corpus falls back to the old template rows in `bulk_generators` and synthetic or bundled heroes.

**Full re-seed** (development or staging: **wipes** seeded application content—confirm backups): `python manage.py reset_microscopis` (this already runs `seed_microscopis` at the end—**do not** run `seed_microscopis` again unless you use `--skip-seed` on reset). Without a populated `IngestedArticle` table, article hero/avatar/Z images are still **generated into** `MEDIA_ROOT` in fallback mode (Pillow by default; optional local SD—see below). After a **complete** full seed, `seed_driftglass` runs; then optional checks: `python manage.py validate_seed_metadata --strict` and `python manage.py validate_seed_metadata --check-themes` (if Driftglass is empty, `--strict` fails until seeding finishes). Flags `--skip-image-check` on reset/seed are **deprecated** (ignored).

### Optional: local Stable Diffusion (`with-sd` profile)

1. **Profile:** `docker compose --profile with-sd up -d --build` starts **`imagegen`** (Diffusers + SD 1.5) and uses the shared **`sd_models`** volume for the Hugging Face cache. The first pull of the model is **large** and slow; CPU inference is usable but **slow** (minutes for large seed batches).
2. **Env (e.g. `.env`):** `SD_ENABLED=1`, `SD_URL=http://imagegen:8080` (Compose sets defaults on `web`). Optional: `SD_MODEL` (default `runwayml/stable-diffusion-v1-5`), `SD_INFERENCE_STEPS` (default `18`). Seeded on-disk heroes use same-origin `/media/…` URLs in the database (see `MEDIA_URL` / `SERVE_MEDIA_THROUGH_DJANGO`).
3. **`web` volume `media_data`** persists generated PNGs at `/app/media`. **`SERVE_MEDIA_THROUGH_DJANGO`** defaults to `1` in Compose so Gunicorn serves `/media/…`; for production behind Nginx/Caddy, prefer serving `MEDIA_ROOT` from the reverse proxy and set `SERVE_MEDIA_THROUGH_DJANGO=0`.
4. **GPU (Linux/NVIDIA):** add a `deploy.resources` / `device_requests` block for the `imagegen` service in your override file (not in the default compose) so the container can see `nvidia-smi`—**optional**; CPU works without it.
5. **Without the profile** (`SD_ENABLED=0` or unset), seeds still succeed using **Pillow** procedural PNGs (CI-friendly; palette and stroke pattern vary by article via a hash of the grounded text snippet when `SEED_IMAGE_GROUNDED=1`).

**Article-grounded prompts (default `SEED_IMAGE_GROUNDED=1`):** seed commands pass title/excerpt into `synthetic_media` so the **SD** (and off-line **Pillow** fallback) is steered by article text, with a small **strip list** of fashion-brand tokens. Tune **`SEED_IMAGE_MAX_PROMPT_WORDS`** and **`SD_DEFAULT_NEGATIVE_PROMPT`** in `.env` to match the `imagegen` service.

**Licensed self-hosted hero images (Wikimedia, etc.):** `python manage.py ingest_sourced_hero` and optional seed fields `sourced_image_url` + `sourced_image_credit` in VERSO/Khula rows call [`docs/AGENT_SOURCING_HEROES.md`](docs/AGENT_SOURCING_HEROES.md). **Guardrails** (defaults if unset in `.env`):

- **`SEED_SOURCED_IMAGE_ALLOW_HOSTS`** — comma-separated hostnames; only those hosts are allowed (prevents the app from being an open image proxy). Set to `upload.wikimedia.org,commons.wikimedia.org,images.unsplash.com` explicitly or extend the list. Use `*` to disable the host check (not recommended in production).
- **`SEED_SOURCED_IMAGE_MAX_BYTES`** — default `5000000` (5 MB).
- **`SEED_SOURCED_IMAGE_TIMEOUT`** — HTTP timeout in seconds; default `60`.

### Pre-rendered / batch “good” images (no inference at seed time)

1. On a **strong** machine, generate the full set once (e.g. `SYNTHETIC_MODE=generate`, `SD_ENABLED=1` with the `with-sd` profile) and run `seed_microscopis` so `media/synthetic/...` fills.
2. Run **`python manage.py export_synthetic_bundles`**, which copies those PNGs into [`assets/seed_heroes/`](assets/seed_heroes/) (see [`assets/seed_heroes/README.md`](assets/seed_heroes/README.md) for required filenames). Commit; use **Git LFS** for `*.png` if the total size is large.
3. In CI or production, set **`SYNTHETIC_MODE=auto`** (default: use a file from `assets/seed_heroes/` if present, otherwise fall back) or **`SYNTHETIC_MODE=offline`** to **require** every bundled file (fails on missing). Optional: `SEED_HEROES_DIR` if the bundle lives outside the default path.

## Application server

**SQLite (default):** use a single worker:

```bash
gunicorn microscopis.wsgi:application --bind 127.0.0.1:8000 --workers 1
```

**PostgreSQL + multiple workers:** you can raise `--workers` (e.g. `3`). If you use more than one worker, set **`REDIS_URL`** so rate limits and the default cache are shared across processes.

### systemd (no Docker)

1. Put env vars in e.g. `/home/deploy/microscopis.com/.env` (not committed); load them in the unit.
2. Example service:

```ini
[Unit]
Description=microscopis (gunicorn)
After=network.target

[Service]
User=deploy
Group=deploy
WorkingDirectory=/home/deploy/microscopis.com
EnvironmentFile=/home/deploy/microscopis.com/.env
ExecStart=/home/deploy/microscopis.com/.venv/bin/gunicorn \
  microscopis.wsgi:application \
  --bind 127.0.0.1:8000 \
  --workers 1
Restart=always

[Install]
WantedBy=multi-user.target
```

3. `sudo systemctl daemon-reload && sudo systemctl enable --now microscopis`
4. Point **Nginx** `proxy_pass` at `http://127.0.0.1:8000` and set `proxy_set_header X-Forwarded-Proto $scheme;` (and usual `Host`, `X-Forwarded-For`).

## Health check

HTTP `GET /health/` returns `200` with body `ok` (no database query).

## Rate limits

`/search/` and `/search/suggest/` enforce per-IP limits (`django-ratelimit`). With **one worker** (recommended for SQLite), in-process cache is enough. With **multiple workers**, set **`REDIS_URL`** or limits are per-worker.
