lista = [1,2,3,4,5]

def kwadrat(x):
    return x ** 2

print(map(kwadrat, lista))
print(list(map(kwadrat, lista)))

print(list(map(lambda x: x + 7, lista)))
print(list(map(lambda x: x ** 3, lista)))

plus5 = lambda x: x + 5

print(list(filter(lambda x: x % 2 == 0, lista)))

# (lambda x, y: print(f"{x + y = }"))(5, 10) # od razu wywołuję funkcję anonimową


def plus4(x):
    print(f"Dodaję 4 do {x}")
    return x + 4

lista = [1,2,3,4]
# for x in [plus4(i) for i in lista]:
for x in map(plus4, lista):
    print("Printuję:")
    print(x)
