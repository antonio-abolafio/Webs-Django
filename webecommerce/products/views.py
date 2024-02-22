from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "products/shop.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "product"

    # Buscar el producto por el nombre
    def get_object(self, queryset=None):
        name = self.kwargs.get("name")
        return Product.objects.get(name=name)


class BrandListView(ListView):
    model = Product
    template_name = "products/category.html"

    def get_queryset(self):
        brand_name = self.kwargs.get("brand")
        return Product.objects.filter(brand__name=brand_name)
