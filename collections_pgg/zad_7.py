"""
Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y)
w podanym przez użytkownika napisie.

1. Pobieramy napis od użytkownika
2. Przechodzimy po kazdej literze z napisu (for)
3. Sprawdzamy czy znak znajduje sie w samogloskach -> tak? to go zliczamy

Jak poradzić sobie ze zliczaniem dużych liter?
1. Możemy je dodać do tupli z samogłoskami
2. Użyć metody .lower()
"""

napis = input('Podaj napis: ')

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
liczba_samoglosek = 0

for litera in napis:
    if litera in samogloski:
        liczba_samoglosek += 1

print(f'W napisie "{napis}" znajduje się {liczba_samoglosek} samoglosek')

