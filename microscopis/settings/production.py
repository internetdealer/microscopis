"""
Production settings: import base, then override for deployment.

Required environment:
  DJANGO_SECRET_KEY
  ALLOWED_HOSTS (comma-separated)

Database:
  DATABASE_URL optional — defaults to SQLite at ``BASE_DIR / db.sqlite3``.
  Override with e.g. ``postgresql://...`` if you use PostgreSQL.
  For SQLite in production, run Gunicorn with **one worker** (see DEPLOY.md).

Strongly recommended:
  CSRF_TRUSTED_ORIGINS (comma-separated full origins, e.g. https://example.com)

Cache:
  REDIS_URL optional — if unset, uses in-process LocMem (fine for a **single** Gunicorn worker).
  For multiple workers + consistent rate limits, set REDIS_URL.

Optional:
  SECURE_HSTS_SECONDS (default 3600; set 0 to disable HSTS)
  DJANGO_SECURE_SSL_REDIRECT (default true; set false for plain HTTP e.g. local Docker)
  SESSION_COOKIE_SECURE / CSRF_COOKIE_SECURE (default true; set false for plain HTTP)
  PUBLIC_CACHE_MAX_AGE (default 300; HTML Cache-Control for anonymous GETs)
"""

from __future__ import annotations

import os
from pathlib import Path

import dj_database_url

from .base import *  # noqa: F403

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("Set DJANGO_SECRET_KEY in the environment for production.")

DEBUG = False

ALLOWED_HOSTS = [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h.strip()]
if not ALLOWED_HOSTS:
    raise ValueError("Set ALLOWED_HOSTS (comma-separated) for production.")

CSRF_TRUSTED_ORIGINS = [
    o.strip() for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()
]

_sqlite_default = "sqlite:///" + Path(BASE_DIR / "db.sqlite3").resolve().as_posix()
DATABASE_URL = os.environ.get("DATABASE_URL", _sqlite_default)

_conn_max_age_env = os.environ.get("DATABASE_CONN_MAX_AGE")
if _conn_max_age_env is not None:
    _conn_max_age = int(_conn_max_age_env)
elif DATABASE_URL.split(":", 1)[0].lower() == "sqlite":
    # Avoid long-lived connections with SQLite; use one Gunicorn worker (DEPLOY.md).
    _conn_max_age = 0
else:
    _conn_max_age = 120

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=_conn_max_age,
        ssl_require=os.environ.get("DATABASE_SSL_REQUIRE", "").lower() in ("1", "true", "yes"),
    )
}

REDIS_URL = os.environ.get("REDIS_URL")
if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "microscopis-prod",
        }
    }

# Celery: use Redis for broker/result when REDIS_URL is set (aligns with cache).
if REDIS_URL:
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", REDIS_URL)

# Shared server-side sessions when Redis is available (multi-worker Gunicorn).
if REDIS_URL:
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"

# Set `SERVE_MEDIA_THROUGH_DJANGO=1` so Gunicorn serves `/media/` (e.g. Docker). On a real VPS,
# prefer Nginx/Caddy `alias` to `MEDIA_ROOT` instead of serving user files through the app process.
SERVE_MEDIA_THROUGH_DJANGO = os.environ.get(
    "SERVE_MEDIA_THROUGH_DJANGO", "false"
).lower() in ("1", "true", "yes")

STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "csp.middleware.CSPMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.public_cache.PublicCacheControlMiddleware",
]

INSTALLED_APPS = list(INSTALLED_APPS) + ["csp"]  # noqa: F405

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = os.environ.get("DJANGO_SECURE_SSL_REDIRECT", "true").lower() in (
    "1",
    "true",
    "yes",
)
# Default True (real HTTPS). Set false for plain HTTP (e.g. local Docker on :8000).
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "true").lower() in (
    "1",
    "true",
    "yes",
)
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", "true").lower() in (
    "1",
    "true",
    "yes",
)
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "3600"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get("SECURE_HSTS_INCLUDE_SUBDOMAINS", "").lower() in (
    "1",
    "true",
    "yes",
)
SECURE_HSTS_PRELOAD = os.environ.get("SECURE_HSTS_PRELOAD", "").lower() in ("1", "true", "yes")
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"

PUBLIC_CACHE_MAX_AGE = int(os.environ.get("PUBLIC_CACHE_MAX_AGE", "300"))

# Per-site CSS still uses Google Fonts via @import; allow those hosts until fonts are self-hosted everywhere.
_GOOGLE_FONTS = ("https://fonts.googleapis.com",)
_GOOGLE_STATIC_FONTS = ("https://fonts.gstatic.com",)

CONTENT_SECURITY_POLICY = {
    # Django admin uses patterns that are painful to align with a strict CSP; keep the surface on public pages.
    "EXCLUDE_URL_PREFIXES": [f"/{ADMIN_URL}/"],
    "DIRECTIVES": {
        "default-src": ["'self'"],
        "script-src": ["'self'", "'unsafe-inline'"],
        "style-src": ["'self'", "'unsafe-inline'", *_GOOGLE_FONTS],
        "img-src": ["'self'", "data:", "https:"],
        "font-src": ["'self'", *_GOOGLE_STATIC_FONTS],
        "connect-src": ["'self'"],
        # Static site: Internet Archive audio embeds (e.g. sites/static/detail.html iframe).
        # default-src is 'self' only, so without frame-src the browser blocks the embed.
        "frame-src": ["'self'", "https://archive.org", "https://www.archive.org"],
        "base-uri": ["'self'"],
        "form-action": ["'self'"],
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std": {
            "format": "{levelname} {asctime} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "std",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.environ.get("LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
