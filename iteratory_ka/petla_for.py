lista = [10, 20, 30]
for x in lista:
    print(x)

it = iter(lista) # wywoła lista.__iter__() ; zwraca iterator, czyli obiekt, który pamięta, który element listy ma zostać zwrócony jako następny
print(it)

x = next(it) # it.__next__()
print(x)
print(next(it))
print(next(it))
# print(next(it)) # StopIteration

it = iter(lista)
while True:
    try:
        e = next(it)
        print("---", e)
    except StopIteration:
        break