from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def players(request):
    return render(request, "core/players.html")


def matches(request):
    return render(request, "core/matches.html")
