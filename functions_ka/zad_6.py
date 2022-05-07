# Zaimplementuj funkcję spłaszczającą podaną listę.
# Przykład użycia:
# >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
# [1, 2, 3, 4, 5, 6, 7]

# isinstace(zmienna, typ) - sprawdza, czy `zmienna` jest typu `typ`

def splaszcz(lista):
    pass

def test_simple():
    assert splaszcz([1,2,3,4]) == [1,2,3,4]

def test_pojedyncze_zagniezdzenie():
    assert splaszcz([1, [2, 3], 4, [5, 6], 7]) == [1,2,3,4,5,6,7]

def test_zadanie():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1,2,3,4,5,6,7]
