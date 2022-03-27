badanie = int(input("W skali od 1 do 10 jak bardzo poleciłbys szkolenie w ALX: "))

if badanie >= 1 and badanie <= 10:
    if badanie >= 9:
        print("promotorzy")
    elif badanie >= 7:
        print("neutralni")
    else:
        print("detraktorzy")
else:
    print('Podaj wartosc z zakresu 1-10')
