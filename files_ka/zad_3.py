# Napisz program wczytujący listę adresów email z pliku i tworzący
# nowy plik z odfiltrowaną zawartością.
# Wejściowy plik może zawierać duplikaty adresów, ten sam adres
# pisany różną wielkością liter, linie zawierające białe znaki oraz
# błędne adresy email (brak znaku @ lub występuje on wiele razy).
# Wynikowy plik powinien zawierać unikalne, posortowane, poprawne
# adresy email.

# with open("emails.txt") as plik_in:
#     with open("clean_emails.txt", 'w') as plik_out:
#         plik_out.write("\n".join(sorted({w.strip().lower() for w in plik_in.read().split('\n') if w.count('@') == 1})))

with open("emails.txt") as plik_in:
    tresc = plik_in.read().split('\n')

zbior = set()
for wiersz in tresc:
    if wiersz.count('@') == 1:
        zbior.add(wiersz.strip().lower())

with open("clean_emails.txt", 'w') as plik_out:
    for email in sorted(zbior):
        plik_out.write(email)
        plik_out.write('\n')
