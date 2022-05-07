class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN")


woda = Product(id=1, name="Woda", price=10.99)
chleb = Product(2, "Chleb", 3.50)
woda.print_info()
chleb.print_info()
