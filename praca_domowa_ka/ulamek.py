def nwd(a, b):
    # algorytm Euklidesa
    if b == 0:
        return a
    return nwd(b, a % b)

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.skroc()

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __imul__(self, other): # a *= b
        self.licznik *= other.licznik
        self.mianownik *= other.mianownik
        self.skroc()
        return self

    def __iadd__(self, other): # a += b
        self.licznik = self.licznik * other.mianownik + self.mianownik * other.licznik
        self.mianownik *= other.mianownik
        self.skroc()
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

    def __rmul__(self, other): # other * self; wywoła się tylko, jeśli `other` nie wspiera __mul__() z typem `self`a
        return self * other # to wywoła self.__mul__(other)

    # def czy_mniejsze_od(self, other):
    def __lt__(self, other): # self < other
        if isinstance(other, Ulamek):
            return self.licznik * other.mianownik < other.licznik * self.mianownik
        elif isinstance(other, int):
            return self.licznik < other * self.mianownik

    def __gt__(self, other): # self > other
        if isinstance(other, Ulamek):
            return other < self
        elif isinstance(other, int):
            return self.licznik > other * self.mianownik

    def __neg__(self):
        return Ulamek(-self.licznik, self.mianownik)

    def skroc(self):
        n = nwd(self.licznik, self.mianownik)
        self.licznik //= n
        self.mianownik //= n


a = Ulamek(1, 2)
b = Ulamek(2, 3)
print(a)
print(b)

print(a * b)
print(a * 4) # a.__mul__(4)
print(5 * a) # 5.__mul__(a) - nie zadziała, więc wywołyjemy a.__rmul__(5)

g = -b # g = b.__neg__()
print(g)
print(f"{a < b = }")
print(f"{a < 1 = }")
print(f"{1 < a = }") # to wywoła `a > 1`

print(f"{nwd(6, 15) = }")

a = Ulamek(13, 26)
print(f"{a}")
