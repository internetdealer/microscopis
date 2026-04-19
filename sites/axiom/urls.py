from django.urls import path

from sites.axiom import views

app_name = "axiom"

urlpatterns = [
    path("", views.home, name="home"),
    path("law/<slug:slug>/", views.law_detail, name="law"),
]
