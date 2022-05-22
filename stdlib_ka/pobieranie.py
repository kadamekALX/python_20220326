from urllib.request import urlopen
import json

# with urlopen("https://www.kindpng.com/picc/m/5-51409_meme-sad-frog-clipart-sad-frog-hd-png.png") as plik:
#     tresc = plik.read()
#
# print(type(tresc))
# # print(tresc)
# with open("zaba.png", 'wb') as plik:
#     plik.write(tresc)
topCount = 10
with urlopen(f"http://api.nbp.pl/api/cenyzlota/last/{topCount}?format=json") as plik:
    lista = json.load(plik)
print(lista)

with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
    lista = json.load(plik)
print("Aktualna cena złota:", lista[0]['cena'])
