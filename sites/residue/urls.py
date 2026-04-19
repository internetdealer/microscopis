from django.urls import path

from sites.residue import views

app_name = "residue"

urlpatterns = [
    path("", views.home, name="home"),
    path("fragment/<slug:slug>/", views.entry_detail, name="fragment"),
]
