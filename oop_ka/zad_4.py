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

class WpisKoszyka:
    def __init__(self, p, ilosc):
        self.produkt = p
        self.ilosc = ilosc

    def wartosc(self):
        return self.produkt.cena * self.ilosc

    def info(self):
        return f"{self.produkt.nazwa}, {self.produkt.cena} x {self.ilosc}"

    def czy_zawiera(self, prod: Produkt):
        return self.produkt == prod


class Koszyk:
    def __init__(self):
        self.zawartosc = {}

    def dodaj_produkt(self, p: Produkt, ile=1):
        if not isinstance(p, Produkt):
            print("Do koszyka można wkładać tylko Produkty!")
            return
        if p.id in self.zawartosc:
            self.zawartosc[p.id].ilosc += ile
        else:
            self.zawartosc[p.id] = WpisKoszyka(p, ile)

    def laczna_wartosc(self):
        suma = 0
        for id, wpis in self.zawartosc.items():
            suma += wpis.wartosc()
        return suma

    def rachunek(self):
        print("Produkty w koszyku:")
        for id, wpis in self.zawartosc.items():
            print(f" - {wpis.info()}")
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
koszyk.dodaj_produkt(woda, 12)
koszyk.dodaj_produkt(woda, 13)
koszyk.dodaj_produkt(bulka)
koszyk.rachunek()