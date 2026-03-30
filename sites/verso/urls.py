from django.urls import path

from sites.verso import views

app_name = "verso"

urlpatterns = [
    path("", views.home, name="home"),
    path("newsletter/", views.newsletter_subscribe, name="newsletter"),
    path("about/", views.about, name="about"),
    path("category/<slug:category>/", views.category_view, name="category"),
    path("article/<slug:slug>/", views.article_detail, name="article"),
]
