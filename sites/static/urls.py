from django.urls import path

from sites.static import views

app_name = "static"

urlpatterns = [
    path("", views.home, name="home"),
    path("signal/<slug:slug>/", views.entry_detail, name="signal"),
]
