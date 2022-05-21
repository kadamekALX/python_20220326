class NieLubieZeraException(Exception):
    pass

def niebezpieczna_funkcja(x):
    if x == 0:
        raise NieLubieZeraException
    return 2 * x + 3

try:
    k = int(input("Podaj k:"))
    x = niebezpieczna_funkcja(k)
    print(x)
    3 / 0
except ValueError as e:
    print("Zlapalem ValueError", e)
except ZeroDivisionError:
    print("Nie dziel przez 0!")
except NieLubieZeraException:
    print("Nie lubimy sie z zerem")

print("reszta programu")

