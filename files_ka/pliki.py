plik = open("plik.txt")
print(plik)
print(plik.read())
plik.seek(4)
# plik.seek(-3, 1) # cofamy kursor o 3 pozycje
print(plik.read())
plik.close()

# plik otwarty w bloku `with` zostanie automatycznie zamknięty
with open("plik.txt") as otwarty_plik:
    tresc = otwarty_plik.read()
print(type(tresc))
print(repr(tresc))