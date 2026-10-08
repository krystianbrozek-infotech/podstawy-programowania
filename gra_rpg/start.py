import random
import funkcje

def przedstawSie(imie, zdrowie, maxZdrowie):
    print(f"Twój bohater nazywa się: {imie}   HP: {zdrowie}/{maxZdrowie}")

def wyprawa(zdrowie):
    print("Wyruszasz na wyprawę...")
    przeciwnik, zdrowiePrzeciwnika, silaPrzeciwnika = funkcje.losujPrzeciwnika()
    print(f"Na Twojej drodze staje {przeciwnik} o sile {silaPrzeciwnika} i zdrowiu {zdrowiePrzeciwnika}")
    return zdrowie - random.randint(0, 2)


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