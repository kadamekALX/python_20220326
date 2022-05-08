class Postac:
    def __init__(self, imie, zdrowie):
        pass

    def wypisz(self):
        pass

    # zmniejsza zdrowie o dmg; zdrowie nie powinno spaść poniżej 0
    def otrzymaj_obrazenia(self, dmg):
        pass

    # przywraca `hp` utraconych punktów zdrowia;
    # zdrowie nie powinno przekroczyć maksymalnej wartosci
    # leczenie nie działa jesli postac nie zyje
    def wylecz(self, hp):
        pass

    # zwraca iformację, czy postać żyje
    def czy_zyje(self):
        pass

rufus = Postac("Rufus", 120)
rufus.wypisz() # Rufus, 120/120 HP
rufus.otrzymaj_obrazenia(15)
rufus.wypisz() # Rufus, 105/120 HP
rufus.wylecz(3)
rufus.wypisz() # Rufus, 108/120 HP
rufus.wylecz(30)
rufus.wypisz() # Rufus, 120/120 HP
rufus.otrzymaj_obrazenia(150)
rufus.wypisz() # Rufus, 0/120 HP / Rufus, nie żyje

p = Postac("Worek treningowy", 100)
while p.czy_zyje():
    p.otrzymaj_obrazenia(7)
    p.wypisz()