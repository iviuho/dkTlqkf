from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignUpView(generic.CreateView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = "/"
