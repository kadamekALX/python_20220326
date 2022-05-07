# Napisz funkcję `zaaplikuj`, ktora przyjmie funkcję `f` oraz listę wartości, a następnie
# zwróci listę wyników funkcji `f` dla wszystkich wartości z listy
# zaaplikuj(f, [a,b,c]) == [f(a), f(b), f(c)]

def zaaplikuj(fun, lista):
    pass

def kwadrat(x):
    return x ** 2

def test_zaaplikuj():
    assert zaaplikuj(kwadrat, [1, 2, 3, 4]) == [1, 4, 9, 16]
