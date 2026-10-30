kolory = ["Zielony", "Niebieski"]
# kolory.append("Zielony")
# kolory.append("Czerwony")
# kolory.append("Niebieski")
# kolory.append("Żółty")

nr=1
for k in kolory:
    print(f"{nr}. {k}")
    nr+=1

wybrany = input("Jaki jest Twój ulubiony kolor?: ")
wyb = int(wybrany)
print(f"Fajno, że lubisz {kolory[wyb-1]}")