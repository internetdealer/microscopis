from django.urls import path

from sites.codex import views

app_name = "codex"

urlpatterns = [
    path("", views.home, name="home"),
    path("entry/<slug:slug>/", views.entry_detail, name="entry"),
]
