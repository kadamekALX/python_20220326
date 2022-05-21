# Zaimplementuj iterator zwracający jedynie samogłoski z zadanego
# ciągu znaków:
# Przykładowe użycie:
# for char in Samogloski("Ala ma kota"):
#     print(char)
# Wynik:
#     A
#     a
#     a
#     o
#     a

class Samogloski:
    def __init__(self, napis):
        self.napis = napis

    def __iter__(self):
        self.indeks = 0
        return self

    def __next__(self):
        while self.indeks < len(self.napis):
            litera = self.napis[self.indeks]
            self.indeks += 1
            if litera.lower() in "aeiouy":
                return litera
        raise StopIteration

for znak in Samogloski("Ala ma kota"):
    print(znak)