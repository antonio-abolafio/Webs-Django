from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Inicio</h1>")


def about(request):
    return HttpResponse("<h1>Historia</h1>")


def services(request):
    return HttpResponse("<h1>Servicios</h1>")


def store(request):
    return HttpResponse("<h1>Tienda</h1>")


def contact(request):
    return HttpResponse("<h1>Contacto</h1>")


def blog(request):
    return HttpResponse("<h1>Blog</h1>")


def sample(request):
    return HttpResponse("<h1>Sample</h1>")
