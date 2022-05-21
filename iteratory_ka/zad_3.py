# Zaimplementuj generator zwracający jedynie samogłoski z zadanego
# ciągu znaków:
# Przykładowe użycie:
# for char in vowels('ala ma kota a kot ma ale'):

def samogloski(napis):
    for litera in napis:
        if litera.lower() in "aeiouy":
            yield litera

for x in samogloski("Ala ma kota"):
    print("samogloska:", x)

print(list(samogloski("Ala ma pieska")))