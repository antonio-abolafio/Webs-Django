from django.urls import path
from .views import ProductListView, ProductDetailView

products_patterns = ([
    path('', ProductListView.as_view(), name='list'),
    path('<str:name>/', ProductDetailView.as_view(), name='detail')
], "products")
