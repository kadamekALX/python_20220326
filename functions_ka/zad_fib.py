# Fib(0) = 0
# Fib(1) = 1
# Fib(n) = Fib(n - 1) + Fib(n - 2)

#     n 0 1 2 3 4 5 6 7  8  9  10
#fib(n) 0 1 1 2 3 5 8 13 21 34 55 ...

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return a

def fib_iter2(n):
    wynik = [0, 1]
    while len(wynik) < n + 1:
        wynik.append(wynik[-1] + wynik[-2])
    return wynik[-1]

def test_fib():
    assert fib(1) == 1
    assert fib(6) == 8

# to się wykona tylko jeśli uruchomimy nasz program bezpośrednio (np. nie podczas testowania)
if __name__ == "__main__":
    n = int(input("Podaj n:"))
    x = fib_iter(n)
    print(x)
    y = fib_iter2(n)
    print(y)

