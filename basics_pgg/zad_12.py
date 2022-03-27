"""
Napisz program obliczający średnią wartość temperatury w danym tygodniu
na podstawie temperatur wprowadzonych przez użytkownika.
"""

numer_dnia = 1
suma_temperatur = 0

while numer_dnia <= 7:
    suma_temperatur += int(input(f'Podaj temperature dla dnia {numer_dnia}: '))
    numer_dnia += 1

srednia_temperatur = suma_temperatur / 7
print(f'Srednia temperatur w tym tygodniu to {srednia_temperatur:.2f}')
