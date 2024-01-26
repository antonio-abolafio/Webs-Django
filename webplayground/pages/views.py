from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page


# Create your views here.
class PagesListView(ListView):
    model = Page
    template_name = "pages/pages.html"
    context_object_name = "pages"

class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page.html"
    context_object_name = "page"
