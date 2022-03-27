"""
Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.
Użytkownik może wprowadzać komendy zmieniające położenie postaci.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku.
Wyjście poza planszę oznacza koniec gry.
Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
Dodatkowo:
- po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym miejscu,
- z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.


ETAP 1 - ruch po planszy
1. zdefiniowane zmienne z pozycją gracza i skarbu (na razie wpisać z palca)
2. trzeba zrobić nieskończoną petle while, gdzie:
- Pokazujemy pozycje gracza
- Zapytać gracza o kierunek (w,s,a,d)
- Zmienic kierunek lub poinformowac, ze kierunek jest nieprawdlowy

ETAP 2 - Sprawdzanie pozycji gracza
1. czy gracz przemiescil sie poza plansze - jesli tak, konczymy gre
2. czy pozycja gracza (x,y) sa takie same jak pozycja skarbu (x,y) - jesli tak, komunikat o wygranej i konczymy gre

ETAP 3 - liczba krokow
1. Zdefiniować zmienna przed petla
2. Po kazdym ruchu ja zwiekszamy
3. Jeżeli gracz wejdzie na skarb, to wysiwetlamy informacje ile ruchow wykonal

ETAP 4 - podpowiedz cieplo, zimno
http://matematyka.pisz.pl/strona/1248.html
1. Policzyc odleglosc miedzy pozycja gracza a skarbu PRZED wykonaniem ruchu.
2. Po wykonaniu ruchu znow liczymy odleglosc
3. Na podstawie roznicy tych dwoch wartosci mowimy czy cieplo czy zimno.

ETAP 5 - nie wyswietlaj podpowiedzi cieplo/zimno z prawdopodobienstwem 1/5
1. uzywamy randint(1,5) i jezeli wylosuje liczbe inna niz 5, to pokazuje podpowiedz

ETAP 6 - przeniesienie skarbu po wykonaniu zbyt duzej liczby ruchow
1. Przed petla while liczymy sobie minimalna odleglosc miedzy graczem a skarbem - mozemy uzyc funkcji abs()
2. Po wykonaniu ruchu sprawdzamy czy liczba_krokow jest wieksza niz dwukrotnosc mininalnej liczby krokow
3. jezeli tak jest, to:
 - losujemy nowa pozycje skarbu (x,y),
 - liczymy na nowo minimalna liczbe krokow
 - zerujemy liczbe wykonanych przez gracza krokow

ETAP 7 - losowanie pozycji gracza i pozycji skarbu na samym poczatku gry
1. Dodać randint przy tworzeniu zmiennych przed petla while
"""
import math

gracz_x = 4
gracz_y = 4

skarb_x = 6
skarb_y = 6

while True:
    print(f'Twoja pozycja x={gracz_x} y={gracz_y}')
    odleglosc_przed_ruchem = math.sqrt((skarb_x-gracz_x)**2 + (skarb_y-gracz_y)**2)

   # ruch gracza
    kierunek = input('Podaj kierunek (w, s, a, d): ')
    if kierunek == 'w':
        gracz_y += 1
    elif kierunek == 's':
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1
    else:
        print('Nieprawidlowy kierunek')
        continue

    odleglosc_po_ruchu = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)

    # sprawdzenie czy gracz wyszedl poza plansza
    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print('Jestes poza plansza! GAME OVER!!!')
        break

    # sprawdzenie czy gracz znalazl skarb
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('BRAWO! WYGRALES! Znalazles skarb')
        break

    if odleglosc_po_ruchu < odleglosc_przed_ruchem:
       print('cieplo')
    else:
       print('zimno')