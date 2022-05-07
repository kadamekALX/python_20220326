# Napisz funkcję `zaaplikuj`, ktora przyjmie funkcję `f` oraz listę wartości, a następnie
# zwróci listę wyników funkcji `f` dla wszystkich wartości z listy
# zaaplikuj(f, [a,b,c]) == [f(a), f(b), f(c)]

def zaaplikuj(fun, lista):
    # return [fun(x) for x in lista]
    wyniki = []
    for x in lista:
        wyniki.append(fun(x))
    return wyniki

def kwadrat(x):
    return x ** 2

def test_zaaplikuj():
    assert zaaplikuj(kwadrat, [1, 2, 3, 4]) == [1, 4, 9, 16]

def plus3(x):
    return x + 3

print(zaaplikuj(kwadrat, [1, 2, 3, 14]))
print(zaaplikuj(plus3, [1, 2, 3, 14]))

# `wybierz` zwraca listę elementow z `lista`, dla których `fun` zwrocilo True
# wybierz(czy_parzysta, [1,2,3,4,5]) == [2, 4]
def wybierz(fun, lista):
    # return [x for x in lista if fun(x)]
    wyniki = []
    for x in lista:
        if fun(x):
            wyniki.append(x)
    return wyniki

def czy_parzysta(x):
    # return x & 1 == 0  # AND bitowy
    return x % 2 == 0

print(wybierz(czy_parzysta, [1,2,3,4,5]))
