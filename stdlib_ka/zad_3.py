# Napisz program z graficznym interfejsem użytkownika (GUI) do
# obliczania kosztów przejazdu na zadanym dystansie na podstawie
# spalania samochodu oraz ceny paliwa.
# Skorzystaj z modułu tkinter.
import tkinter as tk
from tkinter.messagebox import showerror

def oblicz():
    try:
        d = float(dystans_entry.get())
        s = float(spalanie_entry.get())
        c = float(cena_entry.get())
        koszt = d * s * c / 100
        wynik_label.configure(text=f"Koszt przejazdu: {koszt:.2f} PLN")
    except ValueError:
        showerror(title="Error!!!", message="Podano niepoprawną wartość!")

root = tk.Tk()

root.columnconfigure(1, weight=1)

dystans_label = tk.Label(master=root, text="Dystans")
dystans_label.grid(row=0, column=0, sticky=tk.E)
dystans_entry = tk.Entry(master=root)
dystans_entry.grid(row=0, column=1, sticky=tk.EW)

spalanie_label = tk.Label(master=root, text="Spalanie")
spalanie_label.grid(row=1, column=0, sticky=tk.E)
spalanie_entry = tk.Entry(master=root)
spalanie_entry.grid(row=1, column=1, sticky=tk.EW)

cena_label = tk.Label(master=root, text="Cena paliwa")
cena_label.grid(row=2, column=0, sticky=tk.E)
cena_entry = tk.Entry(master=root)
cena_entry.grid(row=2, column=1, sticky=tk.EW)

przycisk = tk.Button(master=root, text="Oblicz", command=oblicz)
przycisk.grid(row=3, column=0)
wynik_label = tk.Label(master=root)
wynik_label.grid(row=3, column=1)

root.mainloop()