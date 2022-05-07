def hello():
    print("No siema")

def witaj(imie):
    print(f"Witaj, {imie}!")

x = hello # zwróć uwagę na brak nawiasów `()`
x()

def wywolaj(fun):
    print("Wywołuję:")
    fun()

wywolaj(hello)

def wywolaj_z_arg(fun, arg):
    print("Wywoluje z argumentem", arg)
    fun(arg)

wywolaj_z_arg(print, "Ala ma kota")

wywolaj_z_arg(wywolaj, hello)

# witaj("Adam")
wywolaj_z_arg(witaj, "Adam")


def lista_dlugosci_n(pobieracz):
    print("Uwaga, generuję listę:")
    return list(range(pobieracz()))

def dziesiec():
    return 10

def pobierz_liczbe_od_usera():
    return int(input("Podaj liczbę:"))

print(lista_dlugosci_n(dziesiec))
print(lista_dlugosci_n(pobierz_liczbe_od_usera))
