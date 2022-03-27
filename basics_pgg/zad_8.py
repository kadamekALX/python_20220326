"""
Napisz program, który zapyta uzytkownika o liczbę całkowitą.
Jeżeli uzytkownik poda liczbę 10, wtedy wyświetl komunikat:
Podałeś szczęśliwy numerek! Wygrałeś!
W przeciwnym wypadku wyświetl:
Spróbuj jeszcze raz!
"""

liczba = int(input('Podaj liczbe calkowita: '))

if liczba == 10:
    print('Podałeś szczęśliwy numerek! Wygrałeś!')
else:
    print('Spróbuj jeszcze raz!')
