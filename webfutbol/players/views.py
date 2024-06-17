from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Player, Statistic


# Create your views here.
class PlayerListView(ListView):
    model = Player
    template_name = "players/players.html"
    context_object_name = "players"


class StatisticDetailView(DetailView):
    model = Statistic
    template_name = "players/statistics.html"
    context_object_name = "statistics"

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Statistic, player__slug=slug)
