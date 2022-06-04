from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from firstApp.models import Produkt

# Create your views here.
def widok(request):
    return HttpResponse(f"Moj pierwszy widok!")

def hello(request, imie, nazwisko="Nowak"):
    return HttpResponse(f"Witaj, {imie} {nazwisko}!")

def dzialanie(request, op, a, b):
    a = int(a)
    b = int(b)
    if op == "dod":
        return HttpResponse(f"{a} + {b} = {a + b}")
    elif op == "ode":
        return HttpResponse(f"{a} - {b} = {a - b}")
    elif op == "mno":
        return HttpResponse(f"{a} * {b} = {a * b}")
    elif op == "dzi":
        if b == 0:
            return HttpResponse("Nie dziel przez 0.")
        return HttpResponse(f"{a} / {b} = {a / b}")
    else:
        return HttpResponse("Błędna operacja!")

def produkty(request):
    # prods = Produkt.objects.all()  # zwraca wszystkie produkty z bazy
    prods = Produkt.objects.filter(dostepny=True)
    return render(request, "lista_produktow.html", context={"produkty": prods})

def szczegoly_produktu(request, id):
    produkt = get_object_or_404(Produkt, id=id) # 404 jesli nie ma takiego produktu
    # produkt = Produkt.objects.get(id=id)
    return render(request, "szczegoly_produktu.html", context={"p": produkt})
