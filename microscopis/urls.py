"""
URL configuration for microscopis project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls.main')),
    path('search/', include('core.urls.search')),
    path('sites/chronicle/', include('sites.chronicle.urls')),
    path('sites/verso/', include('sites.verso.urls')),
    path('sites/', include('sites.urls')),
]
