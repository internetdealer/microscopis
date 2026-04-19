from django.urls import path

from core.views import health_views, main_views

urlpatterns = [
    path("", main_views.home, name="home"),
    path("health/", health_views.health, name="health"),
]
