from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import generic


class SignUpView(generic.FormView):
    pass


def signup(request: WSGIRequest):
    return render(request, "signup.html")


def signin(request: WSGIRequest):
    return render(request, "signin.html")
