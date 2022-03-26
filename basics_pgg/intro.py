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