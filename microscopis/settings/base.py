"""
Shared Django settings for microscopis (imported by local / production).
Does not set SECRET_KEY, DEBUG, or ALLOWED_HOSTS — those belong in the environment-specific module.
"""

import glob
import os
from pathlib import Path

from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def _site_subdirs(name: str) -> list[Path]:
    """Collect sites/<anything>/{name}/ for template and static discovery."""
    pattern = str(BASE_DIR / "sites" / "*" / name)
    return sorted(Path(p) for p in glob.glob(pattern) if Path(p).is_dir())


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Per-site packages (ORM models use Meta.app_label="core"; migrations stay in core)
    "sites.driftglass.apps.DriftglassConfig",
    "sites.gilt.apps.GiltConfig",
    "sites.parlor.apps.ParlorConfig",
    "sites.static.apps.StaticSiteConfig",
    "sites.residue.apps.ResidueConfig",
    "sites.errata.apps.ErrataConfig",
    "sites.axiom.apps.AxiomConfig",
    "sites.codex.apps.CodexConfig",
    "sites.sable.apps.SableConfig",
    "sites.vestige.apps.VestigeConfig",
    "sites.z.apps.ZSiteConfig",
    "core",
    "users",
    "sites.verso.apps.VersoConfig",
    "sites.chronicle.apps.ChronicleConfig",
    "sites.khula.apps.KhulaConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "microscopis.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates", *_site_subdirs("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "microscopis.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

# User-uploaded / seed-generated files (synthetic heroes, avatars, Z media)
MEDIA_URL = (os.environ.get("MEDIA_URL", "/media/") or "/media/").strip()
if not MEDIA_URL.endswith("/"):
    MEDIA_URL += "/"
MEDIA_ROOT = Path(os.environ.get("MEDIA_ROOT", str(BASE_DIR / "media"))).resolve()

# Used by seeding to build absolute image URLs in the database (URLField)
PUBLIC_BASE_URL = (os.environ.get("PUBLIC_BASE_URL", "http://127.0.0.1:8000") or "http://127.0.0.1:8000").rstrip(
    "/"
)

# Pre-rendered hero/media PNGs in git → copied to MEDIA_ROOT at seed (see `assets/seed_heroes/README.md`)
SEED_HEROES_DIR = Path(
    os.environ.get("SEED_HEROES_DIR", str(BASE_DIR / "assets" / "seed_heroes"))
).resolve()

# Web ingest: ``ingest_web_corpus`` → :class:`core.models.IngestedArticle` (pool ``INGEST_OMNI_POOL``).
# Seeds partition that table across sites; set to ``0`` in production when the corpus is fully ingested.
USE_SYNTHETIC_SEED_FALLBACK = os.environ.get("USE_SYNTHETIC_SEED_FALLBACK", "1").lower() in (
    "1",
    "true",
    "yes",
)
INGEST_OMNI_POOL = (os.environ.get("INGEST_OMNI_POOL", "omni") or "omni").strip()
# Order matches partition slices: index ``i`` uses rows [i*100, (i+1)*100) by ``id``.
INGEST_PARTITION_SITE_ORDER: tuple[str, ...] = (
    "verso",
    "khula",
    "chronicle",
    "gilt",
    "parlor",
    "static",
    "residue",
    "errata",
    "axiom",
    "codex",
    "sable",
    "vestige",
    "z",
)

STATICFILES_DIRS = [
    BASE_DIR / "core" / "static",
    *_site_subdirs("static"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Admin URL segment (no leading/trailing slashes), e.g. "admin" -> /admin/
ADMIN_URL = (os.environ.get("DJANGO_ADMIN_URL", "admin") or "admin").strip("/") or "admin"

# Celery: broker from CELERY_BROKER_URL, else REDIS_URL, else local Redis for dev/Docker
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
_CELERY_BROKER = os.environ.get("CELERY_BROKER_URL") or os.environ.get("REDIS_URL")
CELERY_BROKER_URL = _CELERY_BROKER or "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", CELERY_BROKER_URL)
CELERY_BEAT_SCHEDULE = {
    "sync-z-counters": {
        "task": "core.tasks.sync_z_counters",
        "schedule": crontab(minute=0, hour="*"),
    },
}
