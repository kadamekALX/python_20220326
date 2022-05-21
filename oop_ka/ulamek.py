class Ulamek:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ZeroDivisionError("Mianownik nie może być 0")
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __imul__(self, other): # a *= b
        self.licznik *= other.licznik
        self.mianownik *= other.mianownik
        return self

    def __iadd__(self, other): # a += b
        self.licznik = self.licznik * other.mianownik + self.mianownik * other.licznik
        self.mianownik *= other.mianownik
        return self

    def __add__(self, other): # a + b
        licz = self.licznik * other.mianownik + self.mianownik * other.licznik
        mian = self.mianownik * other.mianownik
        return Ulamek(licz, mian) # tworzymy zupełnie nowy Ulamek

    def __mul__(self, other):
        if isinstance(other, Ulamek):
            return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)
        # TODO osobny przypadek jeśli other jest typu int (isinstance(other, int))

    # def czy_mniejsze_od(self, other):
    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

a = Ulamek(1, 2)
b = Ulamek(2, 3)

# if a.czy_mniejsze_od(b):
if a < b: # to jest równoważne a.__lt__(b)
    print(f"{a} jest mniejsze od {b}")
else:
    print(f"{a} nie jest mniejsze od {b}")

print(a)
a *= b #to wykonuje: a = a.__imul__(b)
print(a)
a += b
print(a)
c = a + b # c = a.__add__(b)
print(a, b, c)
d = a + b * c
print(d)

z = 3
e = a * z # to wywoła a.__mul__(z)

# f = 5 * a # TODO (*) doczytac w dokumentacji jak to zrobic

print(b)
# g = -b # TODO zaimplementować __neg__()
# print(g)

x = Ulamek(1, 0)