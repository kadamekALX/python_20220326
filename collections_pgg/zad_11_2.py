"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
Sprawdź jak dużo z tych liczb jest liczbami parzystymi
w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu zbiorów.


1 czesc - ile unikalnych liczb uzytkownik wprowadzil
w petli (while) wczytujemy dane do zbioru, koniec przerywa petle
po petli pokazujemy ile unikalnych liczb zostalo wczytanych i jakie to byly

2 czesc - ile wprowadzonych liczb bylo parzystych w zakresie od 0 do 100
trzeba sobie zrobic zbior liczb parzystych - mozna uzyc petli for i funkcji range(0, 101, 2)
robimy iloczyn teoriomnogosciowy na dwoch zbiorach, zeby pokazac ktore wprowadzone, byly parzyste
"""

liczby_parzyste = set()
for liczba in range(0, 101, 2):
    liczby_parzyste.add(liczba)

liczby_uzytkownika = set()


liczby_str = input('Podaj liczby (np. 1,2,3): ')
lista_liczb_str = liczby_str.split(',')
for liczba_str in lista_liczb_str:
    liczby_uzytkownika.add(int(liczba_str))

print(f'Wprowadzonych unikalnych liczb: {len(liczby_uzytkownika)}')
czesc_wspolna = liczby_parzyste & liczby_uzytkownika
print(f'Wprowadzonych liczb parzystych z zakresu 0-100: {len(czesc_wspolna)}')
