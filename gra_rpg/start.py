import random
import funkcje
#import bohater
from bohater import Bohater
from przeciwnik import Przeciwnik


imie = input("Jak się nazywasz bohaterze? ")
postac = Bohater(imie)

opcja = ""
while opcja != "0":
    print("1. Pokaż bohatera")
    print("2. Wyrusz na wyprawę")
    print("3. Tawerna")
    print("0. Koniec")

    opcja = input("Wybierz opcję: ")
    if opcja == "1":
        postac.przedstawSie()
    elif opcja == "2":
        przeciwnik = Przeciwnik()
        przeciwnik.przedstawSie()
        postac.zdrowie -= 1
        postac.doswiadczenie += przeciwnik.exp