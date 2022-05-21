# Napisz funkcję przyjmij_int(), ktora będzie prosić użytkownika o podanie liczby całkowitej tak długa, aż nie zostanie takowa
# podana. Skorzystaj z mechanizmu wyjątków.

def przyjmij_int():
    while True:
        try:
            x = int(input("Podaj liczbę całkowitą:")) # int() może podnieść ValueError
            return x
        except ValueError:
            print("Podałeś coś co nie jest intem")


# print(float("1.3"))
# print(float("1"))
# print(float("2e4"))

k = przyjmij_int()
print(k)