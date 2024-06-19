from .models import Link

def link_dict(request):
    link = {}
    links = Link.objects.all()
    for l in links:
        link[l.key] = l.url
    return link
