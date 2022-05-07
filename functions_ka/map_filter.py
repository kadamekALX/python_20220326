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
