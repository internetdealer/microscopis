from django.urls import path

from sites.parlor import views

app_name = "parlor"

urlpatterns = [
    path("", views.home, name="home"),
    path("dialogue/<slug:slug>/", views.dialogue_detail, name="dialogue"),
]
