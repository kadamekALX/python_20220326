"""
Napisz program zliczający liczbę wystąpień każdego znaku
w podanym przez użytkownika napisie.


1. Robimy pusty słownik, w którym będziemy zliczać litery
2. Wczytujemy napis od użytkownika
3. Przechodzimy przez wszystkie znaki (for)
  3a. jesli nie ma danego znaku w slowniku to dodajemy go z wartoscia 1
  4b. jezeli jest to zwiększamy liczbe o 1

slownik
klucz  => wartość
litera => liczba wystąpień (int)

Trzeba sprawdzić czy dana litera wystepuje w slowniku!

Podaj napis: Ala
wynik:
{
    'a': 2,
    'l': 1
}
"""

from collections import defaultdict

napis = input('Podaj napis: ')
wystapienia = defaultdict(int)  # slownik z wartoscia domyslna

for litera in napis.lower():
    wystapienia[litera] += 1

for litera, liczba_wystapien in wystapienia.items():
    print(f'{litera} - {liczba_wystapien}')
