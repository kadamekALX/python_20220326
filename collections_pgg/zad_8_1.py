napis = input("podaj napis: ")
lista1 = napis.split("<")
lista2 = lista1[1].split('>')
wyraz = lista2[0]
liczba_znakow = len(wyraz)
print(f'liczba znaków w <> wynosi: {liczba_znakow}')