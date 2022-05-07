# 5! = 1 * 2 * 3 * 4 * 5
# n! = 1 * 2 * ... * n

def silnia(n: int) -> int:
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

print(f"{silnia(5) = }")

# 0! = 1
# n! = n * (n - 1)!

def silnia_rekurencyjna(n: int) -> int:
    if n == 0:
        return 1
    return n * silnia_rekurencyjna(n - 1)

zmienna = 17
x = silnia_rekurencyjna(7)
print(f"{silnia_rekurencyjna(5) = }")