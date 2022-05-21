# Napisz klasy Osoba oraz Dom
# każda osoba mieszka w jakimś Domu (tylko jedym), ale w jednym Domu może mieszkać kilka Osob
# Osoba powinna mieć możliwość zameldowania się w jakimś Domu oraz wymeldowania z niego
# Dom powinien miec możliwość wypisania wszystkich mieszkancow

class Osoba:
    def __init__(self, imie):
        pass

    def wypisz(self): # Jan, mieszka w Domek jednorodzinny
        pass

    def wymelduj(self):
        pass

    def zamelduj(self, dom):
        pass

class Dom:
    def __init__(self, nazwa):
        pass

    def wypisz_mieszkancow(self):
        pass

    def zamelduj(self, osoba):
        pass

    def wymelduj(self, osoba):
        pass


jan = Osoba("Jan")
adam = Osoba("Adam")
jan.wypisz() # Jan, bezdomny
d = Dom("Domek jednorodzinny")
jan.zamelduj(d)
jan.wypisz() # Jan, zamieszkały w: Domek jednorodzinny
adam.zamelduj(d)
d.wypisz_mieszkancow() # Jan, Adam
