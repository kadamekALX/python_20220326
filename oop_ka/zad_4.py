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
    pass

class Koszyk:
    pass


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