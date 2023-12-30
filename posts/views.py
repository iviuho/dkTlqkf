from django.shortcuts import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest):
    return HttpResponse("posts.index")
