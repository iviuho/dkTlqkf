from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "home_index.html"
