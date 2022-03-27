# komentarz, na to python nie patrzy
# string
print("Hello world!")
print('Hello world!')
print('Ksiazka "Pan Tadeusz"')
print("Ksiazka 'Pan Tadeusz'")
print("Ksiazka \"Pan Tadeusz\"")  # "eskejpowanie"
print("A \\n")
print("Pierwsza linia\nDruga linia")
print("Pierwsza liniaDruga linia")
print("""Pierwsza linia
Druga linia""")
print('''Ala
ma
kota''')

# int
print(15)
print(-10)

# float
print(2.5)
print(10 + 2.0)

# liczby zespolone
print(3 + 5j)

# problemy z liczbami ulamkowymi...
print(0.1 * 3.0)

# bool
print(True)
print(False)

# None
print(None)

print()
print("Piotr")
print("Marek", 13)

print(10 + 15)  # wyrazenie z operatorem +

# operatory arytmetyczne
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # dzielenie calkowitoliczbowe
print(10 ** 3)
print(9 ** 0.5)
print(10 % 3)  # modulo, reszta z dzielenia

print("Ala" + "ma kota")  # laczenie napisow, konkatenacja
# print("Ala" + 10)
print("Ala" + str(10))
print("Ala\n" * 5)
print('-' * 60)

# zmienne
imie = 'Piotr'  # = - operator przypisania, == UWAGA! robi coś innego!!!
print(imie)
print(type(imie))

imie = 44
print(imie)
print(type(imie))

# schemat nazywania zmiennych - PEP8 https://peps.python.org/pep-0008/
imie_i_nazwisko = 'Piotr Grabski-Gradzinski'

imie_i_nazwisko = 44

print('-' * 60)

# wczytywanie danych od uzytkownika
# imie = input('Podaj imie: ')  # input zawsze zwraca str!
# print(imie)
# print(type(imie))

print('-' * 60)

# operatory porownania - daje nam True albo False
print(1 == 1)  # True, a rowne b
print(1.0 == 1)  # True
print("1" == 1)  # False
print(int("1") == 1)  # True
print(1 != 1)  # False, a rozne od b
print(1 > 1)  # False, a wieksze od b
print(1 >= 1)  # True, a wieksza badz rowne b
print(1 < 1)  # False
print(1 <= 1)  # True

print('-' * 60)

# operatory logiczne
print(True and True)  # True, i, koniunkcja
print(True or False)  # True, lub, alternatywa
print(not True)  # False, przeczenie

print('-' * 60)

print(9 % 3)  # reszta z dzielenia: 0
print(10 % 3)  # reszta z dzielenia: 1



