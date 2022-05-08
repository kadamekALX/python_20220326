class MojaKlasa:
    POLE_KLASOWE = 100

    def __init__(self, x):
        self.atrybut = x


print(f"{MojaKlasa.POLE_KLASOWE = }")

a = MojaKlasa(5)
b = MojaKlasa(10)

MojaKlasa.POLE_KLASOWE = 200
# a.POLE_KLASOWE = 300 # w ten sposób nie zmienimy wartosci pola klasowego, a ustawimy atrybut w obiekcie a

print(f"{MojaKlasa.POLE_KLASOWE = }")
print(f"{a.atrybut = }")
print(f"{b.atrybut = }")
print(f"{a.POLE_KLASOWE = }")
print(f"{b.POLE_KLASOWE = }")
print(f"{MojaKlasa.POLE_KLASOWE = }")
