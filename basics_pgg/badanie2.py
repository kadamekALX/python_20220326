badanie = int(input("W skali od 1 do 10 jak bardzo poleciłbys szkolenie w ALX: "))

if badanie >= 9:
    print("promotorzy")
elif badanie >=7:
    print("neutralni")
else:
    print("detraktorzy")
