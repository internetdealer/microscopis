from django.urls import path

from sites.z import views

app_name = "z"

urlpatterns = [
    path("", views.home, name="home"),
    path("explore/", views.explore, name="explore"),
    path("activity/", views.activity, name="activity"),
    path("agent/", views.redirect_legacy_agent, name="agent_relay_legacy"),
    path("people/", views.agents_index, name="agents"),
    path("post/<int:pk>/", views.post_detail, name="post"),
    path(
        "user/<str:username>/followers/",
        views.profile_followers,
        name="followers",
    ),
    path(
        "user/<str:username>/following/",
        views.profile_following,
        name="following",
    ),
    path("user/<str:username>/", views.profile, name="profile"),
]
