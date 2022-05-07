# Przyjmij od użytkownika listę intów rozdzieloną przecinkami i zamień
# przyjęty napis na listę intów
# Haczyk: limit wierzy == 1
# "1,2,3,4,5" -> [1,2,3,4,5]

# napis = input("Podaj liczby rozdzielone przecinkami:")
# lista = napis.split(',')
# inty = []
# for s in lista:
#     inty.append(int(s))
# print(inty)

print(list(map(int, input("Podaj liczby rozdzielone przecinkami:").split(','))))

# print(list(filter(lambda znak: znak.isdigit(), input("Podaj ciag znakow:"))))