import json

obiekt = [123, "napis", {"imie": "Adam", "nazwisko": "Małysz"}, True, None]
print(obiekt)
napis = json.dumps(obiekt)
print(napis)
print(type(napis))
with open("plik.json", 'w') as plik:
    plik.write(napis)

with open("plik.json") as plik:
    napis2 = plik.read()

odtworzony = json.loads(napis2)
print(odtworzony)
print(type(odtworzony))
print(odtworzony[1])