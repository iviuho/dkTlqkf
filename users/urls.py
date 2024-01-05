from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", LoginView.as_view(template_name="signin.html"), name="signin"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
