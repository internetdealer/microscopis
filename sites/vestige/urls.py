from django.urls import path

from sites.vestige import views

app_name = "vestige"

urlpatterns = [
    path("", views.home, name="home"),
    path("exhibit/<slug:slug>/", views.exhibit_detail, name="exhibit"),
]
