imie = input("Jak się nazywasz bohaterze? ")
zdrowie = 15
maxZdrowie = 20

opcja = ""
while opcja != "0":
    print("1. Pokaż bohatera")
    print("2. Wyrusz na wyprawę")
    print("0. Koniec")

    opcja = input("Wybierz opcję: ")
    if opcja == "1":
        print(f"Twój bohater nazywa się: {imie}   HP: {zdrowie}/{maxZdrowie}")
    elif opcja == "2":
        zdrowie = zdrowie - 1
        