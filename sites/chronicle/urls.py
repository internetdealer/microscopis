from django.urls import path

from sites.chronicle import views

app_name = "chronicle"

urlpatterns = [
    path("", views.index, name="home"),
    path("tags/", views.tags_list, name="tags"),
    path("tag/<slug:tag_slug>/", views.tag_detail, name="tag"),
    path("entry/<slug:slug>/", views.entry_detail, name="entry"),
]
