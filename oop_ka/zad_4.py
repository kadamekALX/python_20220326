# Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w
# określonej liczbie do koszyka. Zaimplementuj metodę obliczającą
# całkowitą wartość koszyka oraz wypisującą informację o zawartości
# koszyka. Dodanie dwa razy tego samego produktu do koszyka
# powinno stworzyć tylko jedną pozycję.
# Przykład użycia:
# >>> basket = Basket()
# >>> product = Product(1, 'Woda', 10.00)
# >>> basket.add_product(product, 5)
# >>> basket.count_total_price()
# 50.0
# >>> basket.generate_report()
# 'Produkty w koszyku:\n
# - Woda (1), cena: 10.00 x 5\n
# W sumie: 50.00'

class Produkt:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

class Koszyk:
    def __init__(self):
        self.zawartosc = []

    def dodaj_produkt(self, p: Produkt, ile=1):
        if not isinstance(p, Produkt):
            print("Do koszyka można wkładać tylko Produkty!")
            return
        self.zawartosc.append({"produkt": p, "ilosc": ile})

    def laczna_wartosc(self):
        suma = 0
        for prod in self.zawartosc:
            suma += prod["produkt"].cena * prod["ilosc"]
        return suma

    def rachunek(self):
        print("Produkty w koszyku:")
        for p in self.zawartosc:
            print(f" - {p['produkt'].nazwa}, {p['produkt'].cena} x {p['ilosc']}")
        print(f"Suma: {self.laczna_wartosc()} PLN")

# woda = Produkt(1, "Woda", 10)
# banan = Produkt(2, "Banan", 2)
# niewoda = NieProdukt("Woda", 20)
# k = Koszyk()
# k.dodaj_produkt(woda)
# k.dodaj_produkt(banan)
# # k.dodaj_produkt(niewoda)
# print(k.laczna_wartosc())


def test_0():
    woda = Produkt(1, "Woda", 10.50)
    bulka = Produkt(2, "Bułka", 1.75)
    koszyk = Koszyk()
    koszyk.dodaj_produkt(woda)
    koszyk.dodaj_produkt(bulka)
    assert koszyk.laczna_wartosc() == 12.25

def test_1():
    woda = Produkt(1, "Woda", 10)
    bulka = Produkt(2, "Bułka", 1)
    koszyk = Koszyk()
    koszyk.dodaj_produkt(woda, 3)
    koszyk.dodaj_produkt(bulka, 2)
    assert koszyk.laczna_wartosc() == 32


# if __name__ == "__main__":
woda = Produkt(1, "Woda", 10.50)
bulka = Produkt(2, "Bułka", 1.75)
koszyk = Koszyk()
koszyk.dodaj_produkt(woda, 24)
koszyk.dodaj_produkt(bulka)
koszyk.rachunek()