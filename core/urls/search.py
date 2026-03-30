from django.urls import path

from core.views import search_views

urlpatterns = [
    path("", search_views.search, name="search"),
]
