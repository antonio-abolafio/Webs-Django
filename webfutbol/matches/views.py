from django.views.generic.list import ListView
from .models import Match


# Create your views here.
class MatchListView(ListView):

    model = Match
    template_name = "matches/matches.html"
    context_object_name = "matches"