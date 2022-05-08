class Postac:
    def __init__(self, imie, zdrowie):
        self.imie = imie
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie

    def wypisz(self):
        print(f"{self.imie}, {self.zdrowie}/{self.max_zdrowie} HP")

    # zmniejsza zdrowie o dmg; zdrowie nie powinno spaść poniżej 0
    def otrzymaj_obrazenia(self, dmg):
        if dmg < 0:
            self.wylecz(-dmg)
            return
        self.zdrowie -= dmg
        if self.zdrowie < 0:
            self.zdrowie = 0

    # przywraca `hp` utraconych punktów zdrowia;
    # zdrowie nie powinno przekroczyć maksymalnej wartosci
    # leczenie nie działa jesli postac nie zyje
    def wylecz(self, hp):
        if hp < 0:
            self.otrzymaj_obrazenia(-hp)
            return
        if self.czy_zyje():
            self.zdrowie += hp
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie

    # zwraca iformację, czy postać żyje
    def czy_zyje(self):
        return self.zdrowie > 0

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
rufus.wylecz(30)
rufus.wypisz() # Rufus, 0/120 HP / Rufus, nie żyje

p = Postac("Worek treningowy", 100)
while p.czy_zyje():
    p.otrzymaj_obrazenia(7)
    p.wypisz()