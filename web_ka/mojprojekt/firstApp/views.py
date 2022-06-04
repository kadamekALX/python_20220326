from django.shortcuts import render
from django.http import HttpResponse

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

