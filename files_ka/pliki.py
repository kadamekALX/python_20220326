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


with open("wyjscie.txt", "w") as plik: # otwieramy plik do zapisu - jeśli pliku nie ma to zostanie stworzony. Jeśli jest to jego zawartosc jest usuwana
    plik.write("Ala ma kota") # write nie stawia automatycznie '\n'
    plik.write("\n")
    plik.write("Ola ma psa")
