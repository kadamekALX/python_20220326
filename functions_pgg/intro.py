"""
Funkcje

nazwa_funkcji()
print("Ala ma kota")

Z czego sklada sie funkcja:
- sygnatura: nazwa funkcji, argumenty
- ciało funkcji
    - kod ktory ma sie uruchomic kiedy uruchomimy funkcje i zasilimy ja argumentami
    - mozemy zwrocic (nie musimy) jakas wartosc z funkcji
"""

# definicja, deklaracja funkcji
def powiedz_czesc():
    print("Cześć!")
    print('Ala ma kota')

# uruchomienie funkcji
powiedz_czesc()
powiedz_czesc()
powiedz_czesc()

# przekazywanie danych do wnetrza funkcji
# w nawiasach okraglych podajemy argumenty - tutaj na razie jest jeden
# to my decydujemy jak nazywamy argumenty
def powiedz_czesc_komus(imie, nazwisko):
    print(f'Czesc {imie} {nazwisko}')



powiedz_czesc_komus('Piotr', 'GG')
powiedz_czesc_komus('Ala', 'Nowak')


def srednia(liczba1, liczba2):
    c = (liczba1 + liczba2) / 2
    print(c)


srednia(5, 7)
srednia(2, 4)
srednia(10, 4)


def srednia_z_wielu_liczb(liczby):
    wynik = sum(liczby) / len(liczby)
    print(wynik)

srednia_z_wielu_liczb([10, 20 ,30])
srednia_z_wielu_liczb({1, 2, 3})

print('-' * 60)

def srednia_z_wielu_liczb2(liczby):
    wynik = sum(liczby) / len(liczby)
    return wynik
    print('Ala ma kota')  # to sie nie nigdy nie wykona, bo jest po returnie, ktory konczy dzialanie funkcji


policzona_srednia = srednia_z_wielu_liczb2([100, 200, 300])
print(f'Policzona srednia to {policzona_srednia}')

print('-' * 60)


def dodawanio_mnozenie(liczba1, liczba2):
    return (liczba1 + liczba2, liczba1 * liczba2)


wynik = dodawanio_mnozenie(2, 3)
print(wynik)

wynik_dodawania, wynik_mnozenia = dodawanio_mnozenie(4, 5)
print(wynik_dodawania)
print(wynik_mnozenia)

wynik = print('asd')
print(wynik)

print('-' * 60)

# dokumentacja - w jaki sposob mozna dokumentowac swoje funkcje
# type-hinting - podpowiadanie typu
# docstring - tekstowy opis co nasza funkcja robi
def dodawanie(liczba1: int, liczba2: int) -> int:
    """
    Funkcja dodaje do siebie dwie liczby i zwraca ich sumę.

    :param liczba1: Pierwsza liczba do sumy
    :param liczba2: Druga liczba do sumy
    :return: Suma dwoch liczb - liczba1 i liczba2
    """
    return liczba1 + liczba2


wynik = dodawanie(5, 10)
print(wynik)

wynik = dodawanie([1, 2, 3], [4, 5, 6])  # PyCharm podpowiada, ze funkcja dodawanie oczekuje int a my przekazujemy listy i ze to moze byc problemem
print(wynik)












