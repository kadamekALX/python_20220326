class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        # print("Zamieniam na napis")
        return f"{self.nazwa}, cena: {self.cena} PLN"

    def __repr__(self):
        return f"Produkt({self.nazwa!r}, {self.cena})"


p = Produkt("Woda", 12)
# print(p.__str__())
# print(f"Produkt: {p.__str__()}")
# print(p)
# print(str(p)) # str(p) -> p.__str__()
# print(p.__str__())

print(p) # używa p.__str__()
lista = [p, p]
print(lista) # str(lista) używa __repr__ na wszystkich jej elementach
