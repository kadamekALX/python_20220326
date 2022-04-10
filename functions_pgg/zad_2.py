"""
Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.
Przykład użycia:
> czy_jest_pierwsza(10)
False
> czy_jest_pierwsza(17)
True

Liczba pierwsza
- bedzie intem
- wieksza od 1
- dzieli sie tylko przez 1 i przez sama siebie
"""
import math

# zaokraglanie
round(2.5)  # zaokragla na zasadach ogolnych, .5 do gory
math.floor(2.5)  # podloga - zaokragla w dol
math.ceil(2.5)  # sufit - zaokragla do gory
math.sqrt(4)

def czy_jest_pierwsza(liczba: int) -> bool:
    """
    Sprawdzenie czy liczba jest pierwsza: wieksza od 1 i podzielna przez 1 i sama siebie.

    :param liczba:
    :return:
    """
    if liczba <= 1:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True


print(czy_jest_pierwsza(-5))
print(czy_jest_pierwsza(3))
print(czy_jest_pierwsza(9))
print(czy_jest_pierwsza(10))
print(czy_jest_pierwsza(17))
