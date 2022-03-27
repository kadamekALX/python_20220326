"""
Napisz program wypisujący wszystkie liczby od 0 do 100,
podzielne przez 3 lub podzielne przez 5. Wypisz także jak dużo
takich liczb wystąpiło w tym przedziale.

Liczby podzielne przez 3 lub 5:
0
3
5
...
96
99
100
W przedziale 0-100 jest 48 liczb podzielnych przez 3 lub 5
"""
ile_liczb = 0
for liczba in range(0, 101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        print(liczba)
        ile_liczb += 1

print(f'W przedziale 0-100 jest {ile_liczb} liczb podzielnych przez 3 lub 5')
