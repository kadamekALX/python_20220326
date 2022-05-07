class Osoba:
    # __init__ - konstruktor; pierwsza metoda wywoływana na obiekcie zaraz po jego stworzeniu
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Cześć! Jestem {self.imie} {self.nazwisko}")

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie


jan = Osoba("Jan", "Kowalski")
ania = Osoba("Anna", "Kowalska")
krzysiek = Osoba("Krzysztof", "Krawczyk")

osoby = []
osoby.append(jan)
osoby.append(ania)
osoby.append(krzysiek)

jan.zmien_imie("Andrzej")

print(osoby)
for x in osoby:
    x.przedstaw_sie()

