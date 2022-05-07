class MojaKlasa:
    def metoda(self, x):
        print(f"Wywołano metodę z argumentem {x}")

class NaszaKlasa:
    def metoda(self, x):
        print("Metoda z NaszaKlasa")

x = MojaKlasa() # tworzy nowy obiekt typu `MojaKlasa`
print(x)
print(type(x))

x.metoda(10)

x = NaszaKlasa()
x.metoda(10)
