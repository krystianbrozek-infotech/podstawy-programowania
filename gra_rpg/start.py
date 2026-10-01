import random

def przedstawSie(imie, zdrowie, maxZdrowie):
    print(f"Twój bohater nazywa się: {imie}   HP: {zdrowie}/{maxZdrowie}")

def wyprawa(zdrowie):
    print("Wyruszasz na wyprawę...")
    print("Na Twojej drodze staje", losujPrzeciwnika())
    return zdrowie - random.randint(0, 2)

def losujPrzeciwnika():
    przeciwnik = random.randint(1, 3)
    if przeciwnik == 1:
        return "Straszliwy Pikaczu Zagłady"
    if przeciwnik == 2:
        return "Zły Czarodziej"
    if przeciwnik == 3:
        return "Wielki Smok"

imie = input("Jak się nazywasz bohaterze? ")
zdrowie = 15
maxZdrowie = 20

opcja = ""
while opcja != "0":
    print("1. Pokaż bohatera")
    print("2. Wyrusz na wyprawę")
    print("3. Tawerna")
    print("0. Koniec")

    opcja = input("Wybierz opcję: ")
    if opcja == "1":
        przedstawSie(imie, zdrowie, maxZdrowie)
    elif opcja == "2":
        zdrowie = wyprawa(zdrowie)
        