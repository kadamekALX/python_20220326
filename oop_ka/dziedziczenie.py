class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}")


class Pracownik(Osoba): # klasa Pracownik dziedziczy po klasie Osoba
    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko) # to wywoła __init__ z nadklasy Pracownika (z klasy Osoba)
        self.stanowisko = stanowisko

    def pracuj(self):
        print("Pracu-pracu")

    def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie} {self.nazwisko}, pracuję jako {self.stanowisko}")


p = Pracownik("Jan", "Kowalski", "spawacz")
p.przedstaw_sie()
p.pracuj()

print(f"{isinstance(p, Pracownik) = }")
print(f"{isinstance(p, Osoba) = }")


def wypisz_imie(ktos):
    if not isinstance(ktos, Osoba):
        print("Do tej funkcji mozna przekazac tylko Osobe")
    else:
        print(ktos.imie)

wypisz_imie(p)
wypisz_imie(Osoba("Adam", "Małysz"))
wypisz_imie(17)