# Deploying microscopis

The usual setup is **no Docker**: Python venv on the server, **Gunicorn** bound to `127.0.0.1`, and **Nginx** (or Caddy) in front for TLS and reverse proxy.

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
