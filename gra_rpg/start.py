import random
import funkcje
#import bohater
from bohater import Bohater
from przeciwnik import Przeciwnik
from bron import Bron


imie = input("Jak się nazywasz bohaterze? ")
postac = Bohater(imie)

postac.plecak.append(Bron("Kije samobije", 5, 2, 0))
postac.plecak.append(Bron("Nóż", 3, 1, 0))

opcja = ""
while opcja != "0":
    print("1. Pokaż bohatera")
    print("2. Wyrusz na wyprawę")
    print("3. Tawerna")
    print("9. Pokaż plecak")
    print("0. Koniec")

    opcja = input("Wybierz opcję: ")
    if opcja == "1":
        postac.przedstawSie()
    elif opcja == "2":
        przeciwnik = Przeciwnik()
        przeciwnik.przedstawSie()
        postac.zdrowie -= 1
        postac.doswiadczenie += przeciwnik.exp
    elif opcja == "9":
        nr = 1
        for bron in postac.plecak:
            print(f"{nr}. {bron.przedstawSie()}")
            nr += 1