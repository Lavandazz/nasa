from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Космическое агентство'
    description = ('Национальное управление по аэронавтике и исследованию космического пространства — ведомство, '
                   'относящееся к федеральному правительству США и подчиняющееся непосредственно президенту США.')
    context = {
        'title': title,
        'description': description,
    }
    return render(request=request, context=context, template_name="index.html")
