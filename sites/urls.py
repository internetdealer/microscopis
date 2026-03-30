from django.urls import path

from sites import views

urlpatterns = [
    path("<slug:slug>/", views.site_router, name="site_detail"),
]
