# Napisz program obsługujący bazę danych pracowników. W bazie
# danych przechowuj imię, nazwisko, email, rok urodzenia, pensję.
# Skorzystaj z modułu json.
# Przykład użycia:
# $ python employees.py
# Co chcesz zrobić? [d - dodaj, w - wypisz] d
# Imie: Jan
# Nazwisko: Nowak
# Rok urodzenia: 1980
# Pensja: 5000.0
# $ python employees.py
# Co chcesz zrobić? [d - dodaj, w - wypisz] w
# Pracownicy:
# - [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN

import json

try:
    with open("pracownicy.json") as plik:
        lista = json.load(plik)
except FileNotFoundError:
    lista = []

op = input("Jaką operację chcesz wykonać? [d-dodaj, w-wypisz]:")
if op == 'd':
    pracownik = {}
    pracownik["imie"] = input("Podaj imie:")
    pracownik["nazwisko"] = input("Podaj nazwisko:")
    pracownik["rok_ur"] = int(input("Podaj rok urodzenia:"))
    pracownik["pensja"] = int(input("Podaj pensję:"))
    lista.append(pracownik)
    with open("pracownicy.json", 'w') as plik:
        json.dump(lista, plik, indent=4)
        # napis = json.dumps(lista)
        # plik.write(napis)
elif op == 'w':
    for nr, p in enumerate(lista, 1):
        print(f"[{nr}] - {p['imie']} {p['nazwisko']}")
else:
    print("Nieprawidłowy wybór:", op)
