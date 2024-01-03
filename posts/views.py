from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def home(request: WSGIRequest):
    return render(request, "home.html")


def detail(request: WSGIRequest, post_id: int):
    return render(request, "detail.html")
