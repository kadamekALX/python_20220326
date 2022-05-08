class Produkt:
    NAST_ID = 1
    # WSZYSTKIE = [] # raczej tak nie robimy, bo obiekty typu Produkt nigdy nie zostaną zwolnione

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
        self.id = Produkt.NAST_ID
        Produkt.NAST_ID += 1
        # Produkt.WSZYSTKIE.append(self)

    def print_info(self):
        print(f"Produkt \"{self.nazwa}\", id: {self.id}, cena: {self.cena} PLN")

a = Produkt("Woda", 12)
b = Produkt("Awokado", 7)
a.print_info()
b.print_info()

for _ in range(10):
    Produkt("coś", 1)
print(f"{Produkt.NAST_ID = }")

# for p in Produkt.WSZYSTKIE:
#     p.print_info()

print(f"{type(a) = }")
print(f"{type(type(a)) = }")
print(f"{type(Produkt) = }")
print(f"{type(type(type(a))) = }")
