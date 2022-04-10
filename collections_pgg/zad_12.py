"""
Stwórz następujące struktury danych korzystając ze skróconej wersji zapisu:
- (a) listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

- (b) zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian
      - w przedziale od -10 do 10
{(-8, 64, -512), (-1, 1, -1), (9, 81, 729), (4, 16, 64), (5, 25, 125), (2, 4, 8), (-9, 81, -729), (3, 9, 27), (-6, 36, -216), (7, 49, 343), (-4, 16, -64), (0, 0, 0), (-7, 49, -343), (10, 100, 1000), (-5, 25, -125), (-2, 4, -8), (8, 64, 512), (-10, 100, -1000), (-3, 9, -27), (6, 36, 216), (1, 1, 1)}

- (c) słownik mapujący napisy na ich długość powstały ze zbioru napisów
{
    'a': 1,
    'Tom': 3,
    'Amy': 3,
    'To be or not to be': 18
}
"""

# listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
a = [liczba / 10 for liczba in range(0, 11)]
print(a)

a = []
for liczba in range(0, 11):
    a.append(liczba / 10)
print(a)

# zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
b = {(liczba, liczba ** 2, liczba ** 3) for liczba in range(-10, 11)}
print(b)

b = set()
for liczba in range(-10, 11):
    b.add((liczba, liczba ** 2, liczba ** 3))
print(b)

# słownik mapujący napisy na ich długość powstały ze zbioru napisów
c_dane = {'a', 'Tom', 'Amy', 'To be or not to be'}  # pozyskanie danych
c = {napis: len(napis) for napis in c_dane}  # przetworzenie danych
print(c)

c = {}
for napis in c_dane:
    c[napis] = len(napis)
print(c)

# pozyskiwanie danych poprzez odpytanie uzytkownika
napis = input("Podaj napis: ")
dane = napis.split(' ')
print(dane)
dlugosc = {napis: len(napis) for napis in dane}
print(dlugosc)
