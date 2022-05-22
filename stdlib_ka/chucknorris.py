from urllib.request import urlopen, Request
import json
import tkinter as tk

h = {"User-Agent": "Turboprzegladarka3000"}
zapytanie = Request("https://api.chucknorris.io/jokes/categories", headers=h)
with urlopen(zapytanie) as plik:
    kategorie = json.load(plik)

root = tk.Tk()

v = tk.StringVar()
v.set(kategorie[0])
wybor = tk.OptionMenu(root, v, *kategorie)
wybor.grid(row=0, column=0)

root.mainloop()