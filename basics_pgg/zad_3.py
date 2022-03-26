"""
Napisz program wyliczający kwotę należną za zakupiony
towar na podstawie ceny za kilogram oraz liczby zakupionych
kilogramów.
Do przechowywania informacji o cenie oraz liczbie kilogramów
użyj zmiennych.
Wypisz wszystkie informacje na konsolę.

Przykładowy komunikat programu:
Podaj cene za kg: 10.0
Podaj wage: 2.5
Należność: 25.0
"""

cena = float(input('Podaj cene za kg: '))
waga = float(input('Podaj wage: '))

naleznosc = round(cena * waga, 2)
print(type(naleznosc))


print('Naleznosc:', naleznosc, 'PLN')  # 3 argumenty przekazane do printa

print('Naleznosc: ' + str(naleznosc) + ' PLN')

naleznosc_napis = 'Naleznosc: ' + str(naleznosc) + ' PLN'
print(naleznosc_napis)  # 1 argument przekazany do printa

# f-string, formatted string, https://docs.python.org/3/library/string.html#format-specification-mini-language
naleznosc = cena * waga
naleznosc_napis = f'Naleznosc: {naleznosc:_^15.2f} PLN'
print(naleznosc_napis)
