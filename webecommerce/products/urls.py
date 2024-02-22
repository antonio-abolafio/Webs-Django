from django.urls import path
from .views import ProductListView, ProductDetailView, BrandListView

products_patterns = ([
    path('', ProductListView.as_view(), name='list'),
    path('brand/<str:brand>/', BrandListView.as_view(), name='brand'),
    path('product/<str:name>/', ProductDetailView.as_view(), name='detail'),
], "products")
