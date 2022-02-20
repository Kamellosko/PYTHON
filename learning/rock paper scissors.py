import random


wybor = input("kamien papier nozyce: ")
if wybor == "kamien":
    komputer=["kamien","papier","nozyce"]
    wybor_komp = random.choice(komputer)
    print("Wybrales: " + wybor + "\nKomputer wybrał: " + wybor_komp)
elif wybor == "papier":
    komputer=["kamien","papier","nozyce"]
    wybor_komp = random.choice(komputer)
    print("Wybrales " + wybor + "\nKomputer wybrał: " + wybor_komp)
elif wybor == "nozyce":
    komputer=["kamien","papier","nozyce"]
    wybor_komp = random.choice(komputer)
    print("Wybrales " + wybor + "\nKomputer wybrał: " + wybor_komp)
else:
    print("Wpisz jeszcze raz")
if wybor==wybor_komp:
    print("Komputer wybrał to samo co to ty, remis!")
elif wybor=="kamien":
    if wybor_komp=="nozyce":
     print("Kamien pokonuje nozyce, wygrales!:)")
    else:
        print("Papier przykrywa kamien, przegrywasz!")
elif wybor=="papier":
    if wybor_komp=="kamien":
     print("Papier zakrywa kamien, wygrales!")
    else:
        print("Nożyce tną papier, przegrywasz!")
elif wybor=="nozyce":
    if wybor_komp =="papier":
     print("Nozyce tna papier, wygyrwasz!")
    else:
        print("Kamien miazdzy nozyce, przegrywasz!")

