from django.urls import path

from sites.driftglass import views

app_name = "driftglass"

urlpatterns = [
    path("", views.home, name="home"),
    path("telemetry/", views.telemetry, name="telemetry"),
    path("probe/<slug:slug>/", views.probe_detail, name="probe"),
]
