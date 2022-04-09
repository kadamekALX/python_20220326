"""
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.

Przykład:
Ala ma <kota>, a kot ma Alę
4

1. Sprawdzam liczbę < i > - powinno ich być po jednym,
      jeżeli liczba tych nawiasów jest inna, to kończę program
2. W pętli sprawdzam czy:
      - mam zliczac
      - mam przestać zliczać
      - czy zliczanie jest włączone i wtedy zliczam
"""

napis = input('Podaj napis: ')

if napis.count('<') != 1 or napis.count('>') != 1:
    print('Nieprawidlowa liczba nawiasow <>')
    exit()  # exit powoduje zamkniecie programu i to chcemy zrobic, bo dane sa nieprawidlowe

# if napis.find('<') > napis.find('>'):
if not (napis.find('<') < napis.find('>')):
    print('Zla kolejnosc nawiasow, najpier < a pozniej >')
    exit()

czy_zliczac = False
liczba_znakow = 0

for litera in napis:
    if litera == '<':
        czy_zliczac = True
    elif litera == '>':
        czy_zliczac = False
    elif czy_zliczac == True:
        liczba_znakow += 1

print(f'W napisie "{napis}" znaleziono {liczba_znakow} znakow')
