from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('players/', views.players, name="players"),
    path('matches/', views.matches, name="matches"),
]