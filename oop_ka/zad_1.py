class Product:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.price = value

    def print_info(self):
        print(f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN")


woda = Product(id=1, name="Woda", value=10.99)
chleb = Product(2, "Chleb", 3.50)
woda.print_info()
chleb.print_info()
