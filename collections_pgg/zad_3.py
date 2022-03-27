"""
Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej
liście liczb całkowitych.
"""

# https://pl.wikipedia.org/wiki/Znak_liczby

liczby = [1, 2, 3, -100, -10, 0, 4]

dodatnie = 0
ujemne = 0

for liczba in liczby:
    if liczba > 0:
        dodatnie += 1
    elif liczba < 0:
        ujemne += 1

print(f'Dodatnich: {dodatnie}')
print(f'Ujemnych: {ujemne}')
