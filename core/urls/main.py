from django.urls import path

from core.views import main_views

urlpatterns = [
    path("", main_views.home, name="home"),
]
