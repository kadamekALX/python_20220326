"""
Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia.

Przykładowy komunikat programu:
Podaj rok urodzenia: 1980
Jesteś pełnoletni!
"""

import datetime

rok_urodzenia = int(input('Podaj rok urodzenia: '))
aktualny_rok = datetime.date.today().year
print(aktualny_rok)
wiek = aktualny_rok - rok_urodzenia

if wiek >= 18:
    print('Jesteś pełnoletni')
else:
    print('NIE jesteś pełnoletni')
