from django.urls import path

from sites.khula import views

app_name = "khula"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.categories_index, name="categories"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("category/<slug:category>/", views.category_view, name="category"),
    path("article/<slug:slug>/", views.article_detail, name="article"),
]
