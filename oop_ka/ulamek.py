class Ulamek:
    def __init__(self, licznik, mianownik):
        pass

    def __str__(self):
        pass

    def domnoz(self, other): # a.domnoz(b) - a *= b
        pass


def test_domnoz():
    a = Ulamek(1, 2)
    b = Ulamek(2, 3)
    a.domnoz(b)
    assert str(a) == "2/6"