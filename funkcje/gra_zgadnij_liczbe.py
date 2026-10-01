#zrób grę, gdzie komputer losuje liczbę od 0 do 100
#gracz podaje liczbę i komputer odpowiada czy jest większa, mniejsza czy równa
#gramy dopóki nie zgadniemy liczby
#na koniec wyświetlamy liczbę prób

import random

losowanie = random.randint(0, 100)
liczba = int(input("Podaj liczbę od 0 do 100: "))
proby = 0
while losowanie != liczba:
    proby = proby + 1
    if liczba < losowanie:
        print("Twoja liczba jest mniejsza od wylosowanej.")
    else:
        print("Twoja liczba jest większa od wylosowanej.")
    liczba = int(input("Podaj liczbę od 0 do 100: "))
print("Zgadłeś!!! Liczba prób: ", proby)
