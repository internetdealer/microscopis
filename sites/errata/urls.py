from django.urls import path

from sites.errata import views

app_name = "errata"

urlpatterns = [
    path("", views.home, name="home"),
    path("timeline/", views.timeline, name="timeline"),
    path("correction/<slug:slug>/", views.entry_detail, name="correction"),
]
