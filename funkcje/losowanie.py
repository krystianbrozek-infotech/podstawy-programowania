import random

losowanie = random.randint(1, 3)
print(losowanie)

wybor = input("Kamień (k), Papier (p), Nożyce (n)")
if wybor == "k" and losowanie == 1:
    print("Remis!")
elif wybor == "k" and losowanie == 2:
    print("Przegrałeś!")
elif wybor == "k" and losowanie == 3:
    print("Wygrałeś!")

#zrób grę, gdzie komputer losuje liczbę od 0 do 100
#gracz podaje liczbę i komputer odpowiada czy jest większa, mniejsza czy równa
#gramy dopóki nie zgadniemy liczby
#na koniec wyświetlamy liczbę prób