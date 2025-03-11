from django.shortcuts import render
from .models import Poema

def lista_poemas(request):
    categoria = request.GET.get('categoria', '')
    poemas = Poema.objects.all()
    if categoria:
        poemas = poemas.filter(categoria=categoria)
    return render(request, 'poemas/poemas.html', {'poemas': poemas, 'categoria': categoria})
