"""
URL configuration for microscopis project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

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
