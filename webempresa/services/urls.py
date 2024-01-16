from django.urls import path
from . import views

urlpatterns = [
    # Paths services
    path('', views.services, name='services'),
]
