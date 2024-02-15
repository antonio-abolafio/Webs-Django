from django.shortcuts import render
from django.views.generic import DetailView, ListView

from products.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "products/shop.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
