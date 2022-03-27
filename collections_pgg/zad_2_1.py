"""
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy. Pozwól na wprowadzenie 10 liczb.
Skorzystaj z funkcji wbudowanej sum().
"""

liczby = []  # [] - tworzy pusta liste

while len(liczby) < 10:
    liczba = int(input('Podaj liczbe: '))
    liczby.append(liczba)

srednia = sum(liczby) / len(liczby)
print(f'Srednia z prowadzonych liczb {liczby} to {srednia:.2f}')
