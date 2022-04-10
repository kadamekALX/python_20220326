"""
Stwórz kalkulator oparty o funkcje:
1. Pobierz od użytkownika 2 liczby
2. Zapytaj o działanie: (+, -, *, /)
3. Na podstawie działania wykonujemy obliczenia i je pokazujemy
"""
from typing import Union

# jezeli chcemy zasugerowac, ze dany argument moze byc podany w kilku typach, to mozemy
# wykorzystac Union[typ1, typ2, typ3] - mowimy wtedy jakie rozne typy sa dozwolone
def suma(liczba_1: Union[int, float], liczba_2: Union[int, float]) -> Union[int, float]:
    return liczba_1 + liczba_2


def roznica(liczba_1: float, liczba_2: float) -> float:
    return liczba_1 - liczba_2


def iloczyn(liczba_1: float, liczba_2: float) -> float:
    """

    :param liczba_1:
    :param liczba_2:
    :return:
    """
    return liczba_1 * liczba_2


def iloraz(liczba_1: float, liczba_2: float) -> float:
    return liczba_1 / liczba_2


liczba_1 = float(input('Podaj pierwszą liczbę: '))
liczba_2 = float(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji (+, -, *, /): ')

if operacja == '+':
    wynik = suma(liczba_1, liczba_2)
elif operacja == '-':
    wynik = roznica(liczba_1, liczba_2)
elif operacja == '*':
    wynik = iloczyn(liczba_1, liczba_2)
elif operacja == '/':
    wynik = iloraz(liczba_1, liczba_2)
else:
    wynik = 'operacja nieprawidlowa'

print(f'Wynik: {liczba_1}{operacja}{liczba_2}={wynik}')