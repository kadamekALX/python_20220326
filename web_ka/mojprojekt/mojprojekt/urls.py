"""mojprojekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from biblioteka.views import *
from firstApp.views import *  # importujemy wszystkie widoki z firstApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('widok/', widok),
    path('hello/<imie>/', hello),
    path('hello/<imie>/<nazwisko>/', hello),
    path('dzialanie/<op>/<a>/<b>/', dzialanie),
    path('produkty/', produkty, name="lista_produktow"),
    path('produkt/<int:id>/', szczegoly_produktu, name="szczegoly_produktu"),
    path('autorzy/', lista_autorow, name="lista_autorow"),
    path('autor/<int:id>/', szczegoly_autora, name="autor_details"),
]
