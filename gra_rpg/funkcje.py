import random

def losujPrzeciwnika():
    zdrowie = 10
    sila = 5
    przeciwnik = random.randint(1, 3)
    nazwa = ""
    if przeciwnik == 1:
        nazwa = "Pikaczu"
        zdrowie += 5 #zdrowie = zdrowie + 5
    elif przeciwnik == 2:
        nazwa = "Czarodziej"
        zdrowie -= 2
        sila -= 1
    else:
        nazwa = "Smok"
        zdrowie += 10
        sila += 3

    przeciwnik = random.randint(1,4)
    if przeciwnik == 1:
        nazwa = "Straszliwy " + nazwa
    elif przeciwnik == 2:
        nazwa = "Zły " + nazwa
    elif przeciwnik == 3:
        nazwa = "Wielki " + nazwa
    else:
        nazwa = "Potężny " + nazwa

    przeciwnik = random.randint(1,2)
    if przeciwnik == 1:
        nazwa = nazwa + " Zagłady"
    else:
        nazwa = nazwa + " Zniszczenia"

    return nazwa, zdrowie, sila