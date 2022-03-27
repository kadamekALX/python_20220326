"""
Stwórz tuplę zawierającą 10 różnych liczb całkowitych.
Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie)
- co trzeci element
- co drugi element licząc od końca
"""

#    0   1   2   3   4   5   6   7   8   9 -> klucze
x = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#    1   2   3   4   5   6   7   8   9   10 -> który element
#   -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 -> ideksy ujemne

print(x[1])  # 20
print(x[8])  # 90
print(x[-2])  # 90
print(x[2:7])  # 30, 40, 50, 60, 70
print(x[::3])  # 10, 40, 70, 100
print(x[::-2])  # 100, 80, 60, 40, 20
