from django.shortcuts import render

from main.models import SpaceImage


# Create your views here.


def index(request):
    title = 'Космическое агентство'
    description = ('Национальное управление по аэронавтике и исследованию космического пространства — ведомство, '
                   'относящееся к федеральному правительству США и подчиняющееся непосредственно президенту США.')
    slides = SpaceImage.objects.all()
    context = {
        'title': title,
        'description': description,
        'slides': slides
    }
    return render(request=request, context=context, template_name="index.html")
