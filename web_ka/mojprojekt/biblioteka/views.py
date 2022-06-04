from django.shortcuts import render, get_object_or_404
from biblioteka.models import Autor, Ksiazka, AutorForm

# Create your views here.

def lista_autorow(request):
    autorzy = Autor.objects.all()
    if request.method == 'POST':
        pass # TODO doczytac jak dodac nowego autora z formularza
    form = AutorForm()
    return render(request, "lista_autorow.html", context={"autorzy": autorzy, "form":form})

def szczegoly_autora(request, id):
    autor = Autor.objects.get(id=id)
    # wszystkie ksiazki, ktorych autor ma zadane ID
    ksiazki = Ksiazka.objects.filter(autor__id=id)
    return render(request, "szczegoly_autora.html", context={"autor": autor, "ksiazki": ksiazki})