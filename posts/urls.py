from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:post_id>/", views.detail, name="detail"),
]
