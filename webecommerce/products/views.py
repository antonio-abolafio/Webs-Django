from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "products/shop.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"

    # Buscar el producto por el nombre
    def get_object(self, queryset=None):
        name = self.kwargs.get("name")
        return get_object_or_404(Product, name=name)
