from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def widok(request):
    return HttpResponse(f"Moj pierwszy widok!")

def hello(request, imie, nazwisko="Nowak"):
    return HttpResponse(f"Witaj, {imie} {nazwisko}!")