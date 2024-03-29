# Napisz klasy Osoba oraz Dom
# każda osoba mieszka w jakimś Domu (tylko jedym), ale w jednym Domu może mieszkać kilka Osob
# Osoba powinna mieć możliwość zameldowania się w jakimś Domu oraz wymeldowania z niego
# Dom powinien miec możliwość wypisania wszystkich mieszkancow

class Osoba:
    def __init__(self, imie):
        self.imie = imie
        self.adres = None

    def wypisz(self): # Jan, mieszka w Domek jednorodzinny
        if self.adres is None:
            print(f"{self.imie}, bezdomny")
        else:
            print(f"{self.imie}, mieszka w {self.adres}")

    def wymelduj(self):
        if self.adres is not None:
            self.adres._wymelduj(self)
        self.adres = None

    def zamelduj(self, dom):
        self.wymelduj()
        if dom is not None:
            dom._zamelduj(self)
        self.adres = dom

class Dom:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.__lokatorzy = [] # pole "prywatne"

    def __str__(self):
        return self.nazwa

    def wypisz_mieszkancow(self):
        print(f"{self.nazwa}:")
        for m in self.__lokatorzy:
            print(f"\t{m.imie}")

    def _zamelduj(self, osoba): # '_' na początku nazwy oznacza, że nie powinno się z tego korzystać poz klasą (chyba, że wiemy co robimy)
        self.__lokatorzy.append(osoba)

    def _wymelduj(self, osoba):
        self.__lokatorzy.remove(osoba)


jan = Osoba("Jan")
adam = Osoba("Adam")
adam.wymelduj()
jan.wypisz() # Jan, bezdomny
d = Dom("Domek jednorodzinny")
jan.zamelduj(d)
jan.wypisz() # Jan, zamieszkały w: Domek jednorodzinny
adam.zamelduj(d)
d.wypisz_mieszkancow() # Jan, Adam
d2 = Dom("Chałupa")
jan.zamelduj(d2)
d2.wypisz_mieszkancow()
d.wypisz_mieszkancow()
jan.zamelduj(None)
jan.wypisz()
print(dir(d))
print(d._Dom__lokatorzy) # da się dobrać do pola prywatnego jak się bardzo chce ;)
