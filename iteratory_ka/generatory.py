def generator_1():
    print("Generuje 1")
    yield 1
    print("Generuje 2")
    yield 2
    print("Generuje 3")
    yield 3
    print("Koniec generatora")

def licznik(n):
    i = 0
    while i < n:
        yield i
        i += 1

def licznik2(n):
    for i in range(n):
        yield i

print(generator_1())
for x in generator_1():
    print(x)

for i in licznik2(4):
    print("---", i)