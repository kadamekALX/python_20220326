# Napisz generator, ktory wygeneruje wszystkie liczby pierwsze

def czy_pierwsza(liczba):
    # if liczba <= 2:
    #     return [False, False, True][liczba]
    if liczba <= 1:
        return False
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    for i in range(3, int(liczba ** 0.5) + 1, 2):
        if liczba % i == 0:
            return False
    return True

def pierwsze():
    liczba = 1
    while True:
        # print(f"Sprawdzam {liczba}")
        if czy_pierwsza(liczba):
            yield liczba
        liczba += 1


#petla nieskonczona wypisujaca po kolei wszystkie liczby pierwsze
# for x in pierwsze():
#     print(x)

# it = pierwsze()
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i, x in enumerate(pierwsze(), 1):
    if x > 100:
        break
    print(f"{i}: {x}")