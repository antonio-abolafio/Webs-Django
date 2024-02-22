from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, BrandListView

products_patterns = ([
    path('', ProductListView.as_view(), name='list'),
    path('product/<str:name>/', ProductDetailView.as_view(), name='detail'),
    path('category/<str:category>/', CategoryListView.as_view(), name='category'),
    path('brand/<str:brand>/', BrandListView.as_view(), name='brand'),
], "products")
