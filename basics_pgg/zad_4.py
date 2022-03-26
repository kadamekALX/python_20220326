"""
Napisz program obliczający koszt przejazdu z miasta A do B na
podstawie podanej
przez użytkownika liczby kilometrów, ceny paliwa oraz spalania.
Zapytaj użytkownika także o nazwy miejscowości.

Przykładowe komunikaty programu:
Podaj miasto A: Warszawa
Podaj miasto B: Gdańsk
Podaj dystans Warszawa-Gdańsk: 420
Podaj cene paliwa: 4.55
Spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105.11 PLN

100 km  - spalanie
dystans - x
"""
miasto_a = input('Podaj miasto A: ')
miasto_b = input('Podaj miasto B: ')
dystans = float(input(f'Podaj dystans {miasto_a}-{miasto_b}'))
cena = float(input('Podaj cene paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))

koszt = dystans * spalanie / 100.0 * cena

print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN')
