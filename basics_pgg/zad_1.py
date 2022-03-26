# zad_1.py
"""
Korzystając z przypisywania wartości do zmiennych,
napisz program obliczający pole trapezu
o długości podstaw 3 i 9 oraz wysokości 6.5.
"""

podstawa_a = 3
podstawa_b = 9
wysokosc = 6.5

# kolejnosc wykonywania operatorow: https://docs.python.org/3/reference/expressions.html#operator-precedence
pole_trapezu = 1 / 2 * (podstawa_a + podstawa_b) * wysokosc
print(pole_trapezu)
