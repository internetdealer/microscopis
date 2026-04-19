from django.urls import path

from sites.sable import views

app_name = "sable"

urlpatterns = [
    path("", views.home, name="home"),
    path("theory/<slug:slug>/", views.theory_detail, name="theory"),
]
