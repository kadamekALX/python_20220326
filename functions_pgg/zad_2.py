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


def test_przykladowy():
    # assert, po polsku asercja
    assert czy_jest_pierwsza(-5) == False

    # podejscie GWT - Given When Then
    liczba = -5 # given
    wynik = czy_jest_pierwsza(liczba)  # when
    assert wynik == False  # then

def test_liczb_pierwszych():
    liczby_pierwsze = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    for liczba in liczby_pierwsze:
        assert czy_jest_pierwsza(liczba) == True

def test_licz_nie_pierwszych():
    liczby_nie_pierwsze = [-100, -10, -1, 0, 1, 4, 9, 15, 24, 36, 100]
    for liczba in liczby_nie_pierwsze:
        assert czy_jest_pierwsza(liczba) == False
