from django.urls import path
from .views import MatchListView

urlpatterns = [
    # Matches paths
    path('', MatchListView.as_view(), name="matches"),
]
