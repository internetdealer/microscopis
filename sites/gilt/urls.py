from django.urls import path

from sites.gilt import views

app_name = "gilt"

urlpatterns = [
    path("", views.home, name="home"),
    path("entry/<slug:slug>/", views.entry_detail, name="entry"),
]
