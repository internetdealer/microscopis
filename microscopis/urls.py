"""
URL configuration for microscopis project.
"""

import re
from urllib.parse import urlsplit

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

_admin = getattr(settings, "ADMIN_URL", "admin").strip("/") or "admin"

urlpatterns = [
    path(f"{_admin}/", admin.site.urls),
    path('', include('core.urls.main')),
    path('search/', include('core.urls.search')),
    path('sites/driftglass/', include('sites.driftglass.urls')),
    path('sites/gilt/', include('sites.gilt.urls')),
    path('sites/parlor/', include('sites.parlor.urls')),
    path('sites/static/', include('sites.static.urls')),
    path('sites/residue/', include('sites.residue.urls')),
    path('sites/errata/', include('sites.errata.urls')),
    path('sites/axiom/', include('sites.axiom.urls')),
    path('sites/codex/', include('sites.codex.urls')),
    path('sites/sable/', include('sites.sable.urls')),
    path('sites/vestige/', include('sites.vestige.urls')),
    path('sites/z/', include('sites.z.urls')),
] + [
    path('sites/chronicle/', include('sites.chronicle.urls')),
    path('sites/verso/', include('sites.verso.urls')),
    path('sites/khula/', include('sites.khula.urls')),
    path('sites/', include('sites.urls')),
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns

# `django.conf.urls.static.static` is a no-op when DEBUG is False, so in Docker/production
# we must wire `serve` ourselves when `SERVE_MEDIA_THROUGH_DJANGO` is set.
_serve_media = settings.DEBUG or getattr(
    settings, "SERVE_MEDIA_THROUGH_DJANGO", False
)
if _serve_media and settings.MEDIA_URL and not urlsplit(settings.MEDIA_URL).netloc:
    _prefix = settings.MEDIA_URL.lstrip("/")
    urlpatterns += [
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(_prefix),
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]
