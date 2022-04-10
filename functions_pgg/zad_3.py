"""
Napisz funkcję zwracającą zbiór wszystkich znaków
występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:
> wiecej_niz('ala ma kota a kot ma ale', 3) -> {'a', ' '}

1. Definiujemy funkcje
2. Policzyc ile jest znakow (.count()) i dodac je do zbioru,
ktory na koncu zwracamy

Przypadki testowe?
pusty napis
2 dowolne napisy
"""

# TDD - Test Driven Development

def wiecej_niz(napis: str, ile_znakow: int) -> set:


def test_pusty_napis():
    assert wiecej_niz('', 1) == set()

def test_pierwszy_napis():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}
