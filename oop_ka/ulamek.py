class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def domnoz(self, other): # a.domnoz(b) - a *= b
        self.licznik *= other.licznik
        self.mianownik *= other.mianownik

    def dodaj(self, other): # a.dodaj(b) - a += b
        self.licznik = self.licznik * other.mianownik + self.mianownik * other.licznik
        self.mianownik *= other.mianownik


a = Ulamek(1, 2)
b = Ulamek(2, 3)
print(a)
a.domnoz(b)
print(a)
a.dodaj(b)
print(a)
