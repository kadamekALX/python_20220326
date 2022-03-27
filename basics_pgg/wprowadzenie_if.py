liczba = int(input('Podaj liczbe: '))

print('Jestem przed ifem')

if liczba == 10:
    print('Brawo! Wygrales!')
    print('Podales liczbe 10')
elif liczba == 15: # elif = else if
    print('No to teraz podales 15, ale sprobuj jeszcze raz')
elif liczba == 20:
    print('Podales 20')
else:
    print('Zaden z warunkow nie zostal spelniony')

print('Jestem po ifie')