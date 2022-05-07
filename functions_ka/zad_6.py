# Zaimplementuj funkcję spłaszczającą podaną listę.
# Przykład użycia:
# >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
# [1, 2, 3, 4, 5, 6, 7]

# isinstance(zmienna, typ) - sprawdza, czy `zmienna` jest typu `typ`
# if isinstance([1,2,3], list):
#     print("[1,2,3] jest typu `list`")

# lista = [1, 4.5, "asdf", 4, 5, 3.14, "qwer", "zxcv"]
# wynik = {}
# for x in lista:
#     if type(x) in wynik:
#         wynik[type(x)].append(x)
#     else:
#         wynik[type(x)] = [x]

def s(lista):
    while True:
        wynik = []
        czy_lista_w_liscie = False
        for x in lista:
            if isinstance(x, list):
                czy_lista_w_liscie = True
                wynik.extend(x)
            else:
                wynik.append(x)
        if czy_lista_w_liscie:
            lista = wynik
        else:
            return wynik

def splaszcz(lista):
    wynik = []
    for element in lista:
        if isinstance(element, (list,tuple)):
            # wynik.extend(splaszcz(element))
            splaszczona = splaszcz(element)
            for x in splaszczona:
                wynik.append(x)
        else:
            wynik.append(element)
    return wynik


def test_simple():
    assert splaszcz([1,2,3,4]) == [1,2,3,4]

def test_pojedyncze_zagniezdzenie():
    assert splaszcz([1, [2, 3], 4, [5, 6], 7]) == [1,2,3,4,5,6,7]

def test_zadanie():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1,2,3,4,5,6,7]


if __name__ == "__main__":
    print(s([1, 2, [3, 4], 5]))
    print(s([1, 2, [[[[[[[[[[[[[[[[[[3, [4, 777]]]]]]]]]]]]]]]]]]], 5]))