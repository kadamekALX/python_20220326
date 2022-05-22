# Pobierz losowy dowcip o Chucku Norrisie ze strony https://api.chucknorris.io/  z wybranej prez użytkownika kategorii
# Przed pobraniem kategorii wyświetl listę wszystkich kategorii.

from urllib.request import urlopen, Request
import json

h = {"User-Agent": "Turboprzegladarka3000"}
zapytanie = Request("https://api.chucknorris.io/jokes/categories", headers=h)
with urlopen(zapytanie) as plik:
    kategorie = json.load(plik)
print(f"Dostępne kategorie: {' '.join(kategorie)}")
wybor = input("Wprowadz wybor:")
if wybor not in kategorie:
    exit(1)

zapytanie = Request(f"https://api.chucknorris.io/jokes/random?category={wybor}", headers=h)
with urlopen(zapytanie) as plik:
    zart = json.load(plik)
print(zart['value'])