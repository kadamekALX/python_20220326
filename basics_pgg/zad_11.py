"""
Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych
i wypisujący wyniki na konsolę.

Przykładowe uruchomienie programu:
Kwadrat liczby 1 to 1
...
Kwadrat liczby 10 to 100
...
Kwadrat liczby 100 to 10000
"""
i = 1
while i <= 100:
    print(f'Kwadrat liczby {i} to {i ** 2}')
    # i = i + 1
    i += 1 # robi dokladnie to samo co i = i + 1, mamy tez -=, *=, /=