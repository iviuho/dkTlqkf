from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import generic

from . import models


class HomeView(generic.ListView):
    template_name = "home.html"

    def get_queryset(self):
        return models.Post.objects.order_by("-created_at")


def detail(request: WSGIRequest, post_id: int):
    return render(request, "detail.html")
