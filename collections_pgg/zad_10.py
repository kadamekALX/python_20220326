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

napis = input('Podaj napis: ')
wystapienia = {}

try:
    if len(napis) > 1:
        pass  # pass - "null operation" - operacja, ktora nic nie robi
except ValueError:
    pass  # jak nie chce nic robic, kiedy powstanie wyjatek (Error)

for litera in napis.lower():
    if litera not in wystapienia:
        wystapienia[litera] = 1
    else:
        wystapienia[litera] += 1

for litera, liczba_wystapien in wystapienia.items():
    print(f'{litera} - {liczba_wystapien}')
