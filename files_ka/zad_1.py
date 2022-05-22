# Napisz program wypisujący na konsolę zawartość wskazanego pliku
# wraz z numerami linii. Obsłuż sytuację, gdy użytkownik nie poda
# nazwy pliku lub poda błędną nazwę.
# Przykład użycia:
# $ python test.txt
# 1: pierwsza linia pliku
# 2: druga linia pliku

# with open("plik.txt") as plik:
#     tresc = plik.read()
# for i, wiersz in enumerate(tresc.split('\n'), 1):
#     print(f"{i}: {wiersz}")

nazwa_pliku = input("Podaj nazwe pliku:")

try:
    with open(nazwa_pliku) as plik:
        for i, w in enumerate(plik, 1):
            print(f"{i}: {w.rstrip()}")
except FileNotFoundError:
    print("Nie ma takiego pliku!")