"""
Stwórz kalkulator oparty o funkcje:
1. Pobierz od użytkownika 2 liczby
2. Zapytaj o działanie: (+, -, *, /)
3. Na podstawie działania wykonujemy obliczenia i je pokazujemy
"""

liczba_1 = float(input('Podaj pierwszą liczbę: '))
liczba_2 = float(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji (+, -, *, /): ')

if operacja == '+':
    wynik = liczba_1 + liczba_2
elif operacja == '-':
    wynik = liczba_1 - liczba_2
elif operacja == '*':
    wynik = liczba_1 * liczba_2
elif operacja == '/':
    wynik = liczba_1 / liczba_2
else:
    wynik = 'operacja nieprawidlowa'

print(f'Wynik: {liczba_1}{operacja}{liczba_2}={wynik}')