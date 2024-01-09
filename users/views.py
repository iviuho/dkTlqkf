from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignUpView(generic.CreateView):
    template_name = "user_signup.html"
    form_class = UserCreationForm
    success_url = "/"


class UserDetailView(generic.DetailView):
    template_name = "user_detail.html"
    model = get_user_model()
