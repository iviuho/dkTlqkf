from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:post_id>/", views.detail, name="detail"),
]
