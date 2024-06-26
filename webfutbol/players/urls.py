from django.urls import path
from .views import PlayerListView, StatisticDetailView

urlpatterns = [
# Players paths
    path('', PlayerListView.as_view(), name="players"),
    path('<slug:slug>/', StatisticDetailView.as_view(), name="statistics"),
]
