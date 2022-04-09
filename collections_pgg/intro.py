# KOLEKCJE

liczba = 10  # pojedyncza wartosc

# Tupla, krotka (ang. tuple)

#    0   1   2 - indeks
a = (10, 20, 30)
print(type(a))
print(a)

# operator dostepu
print(a[0])

print('-' * 60)

a = (10, True, 'Ala ma kota')
print(a[0])
print(a[1])
print(a[2])
# print(min(a))

print('-' * 60)

a = (10, 20, 30)
print(len(a))
print(min(a))
print(max(a))
print(min(a))
print(sum(a))

print('-' * 60)

# operator dostepu - "na sterydach"
#    0    1    2    3    4    5    6    7    8    9
a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#    -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

# a[start:stop-1:krok]
print(a)
print(a[0])
print(a[1])
print(a[0:2])  # ('a', 'b'), indeksy 0, 1; przedzial lewostronnie domkniety, prawostronnie otwarty
print(a[1:5])  # ('b', 'c', 'd', 'e')
print(a[5:])  # ('f', 'g', 'h', 'i', 'j'), od indeksu 5 do konca
print(a[:5])  # ('a', 'b', 'c', 'd', 'e'), od poczatku do 4 wlacznie (bez 5)
print(a[:])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
i = 1
print(a[i])  # b
print(a[-1])  # j
print(a[-5:-2])  # ('f', 'g', 'h')
print(a[-2:-5])  # () - pusta tupla
print(a[0:-1])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
print(a[-3:])  # ('h', 'i', 'j')
print(a[::2])  # ('a', 'c', 'e', 'g', 'i')
print(a[::-25])  # ('j',)
print(a[::25])  # ('a',)
print(a[::-2])  # ('j', 'h', 'f', 'd', 'b')
print(a[::-1])  # ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')\

print('j' in a)  # True, czy 'j' zawiera sie w kolekcji a
print('j' not in a)  # False, czy 'j' NIE zawiera w kolekcji a

print('-' * 60)

tupla_a = (1, 2, 3)
tupla_b = (4, 5, 6)

tupla_c = tupla_a + tupla_b
print(tupla_c)

tupla_d = tupla_b + tupla_a
print(tupla_d)

tupla_e = tupla_a * 5
print(tupla_e)

print(tupla_e[0])
# tupla_e[0] = 123  # TypeError: 'tuple' object does not support item assignment

print('-' * 60)

# LISTA

lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(type(lista_a))

print(lista_a[0])
print(lista_a[0:3])

lista_a[0] = 11
print(lista_a)

lista_a.append(110)  # dodaje element na koniec listy
print(lista_a)

lista_a.insert(3, 35)
print(lista_a)

lista_a[0:2] = [1, 2]
print(lista_a)

lista_a[0:3] = [1, 2]
print(lista_a)


lista_a[0:2] = [1000, 2000, 3000]
print(lista_a)

print('-' * 60)

i = 1
while i < 3:
    print(i)
    # break
    i += 1
else:
    # to co jest w tym else wykona sie tylko wtedy, kiedy nie przerwe
    # petli za pomoca break
    print('Else po while')


print('-' * 60)


lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
while i < len(lista_a):
    print(lista_a[i])
    i += 1

print('-' * 60)

# to samo, ale przy uzciu petli for
lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for liczba in lista_a:  # element - zmienna tymczasowa, ja ustalam jak sie nazywa
    print(liczba)

print('-' * 60)

# range()

for liczba in range(-2, 3):  # lewostronnie domkniety, prawostronnie otwarty
    print(liczba)

print('-' * 60)

for liczba in range(-10, 11, 2):
    print(liczba)

print('-' * 60)

"""
Co zrobic w sytuacji kiedy chcemy miec w petli for
dostep zarowno do wartosci jak i do indeksu, pod ktorym 
ta wartosc sie znajduje?
"""
#              0   1   2   3   4   5  6
temperatury = [10, 15, 17, -1, -5, 0, 2]
for temperatura in enumerate(temperatury):
    print(f"indeks: {temperatura[0]}, wartosc: {temperatura[1]}")

print('-' * 30)

imie, nazwisko = [123, 456]  # liczba zmiennych i liczba elementow po prawej stronie musi byc taka sama
print(imie)
print(nazwisko)

print('-' * 30)

#              0   1   2   3   4   5  6
temperatury = [10, 15, 17, -1, -5, 0, 2]
# wykorzystujemy rozpakowywanie (unpack)
for indeks, temperatura in enumerate(temperatury):
    print(f"indeks: {indeks}, wartosc: {temperatura}")

print('-' * 60)

napis = 'Ala ma kota. a kot ma KOMPILATOR'

# operator dostepu
print(napis[0])
print(napis[0:5])
print(napis[0:10:2])
print(napis[::-1])  # przydaje sie do sprawdzenia czy zdanie jest palindromem

print(napis.lower())  # ala ma kota. a kot ma kompilator
print(napis.upper())  # ALA MA KOTA. A KOT MA KOMPILATOR
print(napis.capitalize())  # Ala ma kota. a kot ma kompilator
print(napis.title())  # Ala Ma Kota. A Kot Ma Kompilator

print(napis.split())  # ['Ala', 'ma', 'kota.', 'a', 'kot', 'ma', 'KOMPILATOR']
print(napis.split(' '))
print(napis.split('.'))
print(napis.split('a'))

slowa = napis.split(' ')
print(slowa)
print(slowa[0:3])

# scalanie stringow
po_scaleniu = '<-->'.join(['a', 'b', 'c'])
print(po_scaleniu)

po_scaleniu = '<-->'.join("Ala ma kota")  # string zostanie potraktowany jako kolekcja
print(po_scaleniu)

# dodatkowe, przydatne funkcje do stringow
# Wszystkie operacje na stringach zwracaja nowe stringi, nie modyfikuja istniejacych
# stringi, podobnie jak tuple, sa niemutowalne
print(napis)
print(napis.count('a'))
print(napis.index('a'))  # indeks pierwszego wystapienia znaku
print(napis.find('a'))

# print(napis.index('z'))  # jezeli index nie znajdzie danego znaku/napisu, wtedy rzuca wyjatkiem (ValueError)
print(napis.find('z'))  # zwraca -1 jezeli nie znajdzie danego znaku/napisu

print(napis.replace('a', ''))


"""
Slownik, dict (ang. dictionary)
struktura, ktora przechowuje klucz->wartosc
Czym moze byc klucz?
- kazda wartoscia, ktora jest hashowalna, posiada metode __hash__(), czyli np.:
  string, int, float, tupla, boolean
Czym moze byc wartosc?
- czymkolwiek
"""

slownik = {
    'Piotr': 123,
    'Maciej': 156,
    'Iwona': 203,
    1: 555,
    (1,2,3): 'Tomek',
}

print(slownik)
print(slownik['Piotr'])  # dostep do wartosci poprzez slownik[klucz]
print(slownik[1])
print(slownik.keys())
print(slownik.values())

print("Ala ma kota".__hash__())
print("Ala ma kota".__hash__())
print(1.5.__hash__())
print(1.5.__hash__())
print( (1,2,3).__hash__() )
# print( [10, 20, 30].__hash__() )

slownik['Ala'] = 500
print(slownik)

slownik['lista_temperatur'] = [10, 20, 30, 40, 50]
print(slownik)

slownik['Ala'] = 600
print(slownik)

print(slownik['Ala'])
print(slownik.get('Ala'))  # wyciagam wartosc dla klucza 'Ala'

# print(slownik['Krystyna'])  # bedzie wyjatek KeyError
print(slownik.get('Krysyna'))  # jezeli nie bedzie takiego klucza, to dostane None
# drugi argument do .get to tzw. wartosc domyslna
print(slownik.get('Krystyna', -10))  # jesli nie ma klucza w slowniku, oddaj -10
print(slownik.get('Ala', -10))  # jezeli jest klucz w slownik, oddaj jego wartosc


print(slownik.keys())
print(slownik.values())
print(slownik.items())
print(list(slownik.items())[1][1])

for klucz, wartosc in slownik.items():
    print(klucz, wartosc)

