class Ulamek:
    def __init__(self, licznik, mianownik):
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

    def __mul__(self, other): # self. * other
        if isinstance(other, Ulamek):
            return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)
        elif isinstance(other, int):
            return Ulamek(self.licznik * other, self.mianownik)

    def __rmul__(self, other): # other * self
        return self * other # to wywoła self.__mul__(other)

    # def czy_mniejsze_od(self, other):
    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __neg__(self):
        return Ulamek(-self.licznik, self.mianownik)

a = Ulamek(1, 2)
b = Ulamek(2, 3)
print(a)
print(b)

print(a * b)
print(a * 4) # a.__mul__(4)
print(5 * a) # 5.__mul__(a) - nie zadziała, więc wywołyjemy a.__rmul__(5)
# f = 5 * a # TODO (*) doczytac w dokumentacji jak to zrobic

g = -b # g = b.__neg__()
print(g)