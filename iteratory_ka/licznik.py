class Licznik:
    def __init__(self, limit):
        self.limit = limit

    # __iter__() musi zwrocic iterator (obiekt posiadający metodę __next__())
    def __iter__(self):
        print("__iter__()")
        self.nastepna = 0
        return self

    def __next__(self):
        print("__next__()")
        if self.nastepna >= self.limit:
            raise StopIteration
        wynik = self.nastepna
        self.nastepna += 1
        return wynik


licznik = Licznik(5)
for x in licznik:
    print(x)
