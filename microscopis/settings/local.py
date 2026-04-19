"""Local development defaults: DEBUG, SQLite, LocMem cache, debug toolbar."""

import os

from .base import *  # noqa: F403

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-g#1#0n3w3fc*e=rm%xq*#eeoed(+s)#6zomqmk4$@7)un=!!2-",
)

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "microscopis",
    }
}

INTERNAL_IPS = ["127.0.0.1"]

# Optional: install with `pip install -r requirements.txt` (django-debug-toolbar).
try:
    import debug_toolbar  # noqa: F401
except ImportError:
    pass
else:
    INSTALLED_APPS = list(INSTALLED_APPS) + ["debug_toolbar"]  # noqa: F405
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]  # noqa: F405
