import tkinter as tk

def fun():
    print("Przycisk został nacisniety.")
    tresc = pole_tekstowe.get()
    print(f"Tresc pola: {tresc}")
    tekst.configure(text=tresc)

root = tk.Tk()
root.title("Aplikacja okienkowa")
przycisk = tk.Button(master=root, text="Click me!", command=fun)
przycisk.grid(row=0, column=0)

pole_tekstowe = tk.Entry(master=root)
pole_tekstowe.grid(row=1, column=1)

tekst = tk.Label(master=root, text="To jest label")
tekst.grid(row=0, column=1)

root.mainloop()