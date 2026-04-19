"""
Shared Django settings for microscopis (imported by local / production).
Does not set SECRET_KEY, DEBUG, or ALLOWED_HOSTS — those belong in the environment-specific module.
"""

import glob
import os
from pathlib import Path

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
STATICFILES_DIRS = [
    BASE_DIR / "core" / "static",
    *_site_subdirs("static"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Admin URL segment (no leading/trailing slashes), e.g. "admin" -> /admin/
ADMIN_URL = (os.environ.get("DJANGO_ADMIN_URL", "admin") or "admin").strip("/") or "admin"
