for krok in range(5):
    print("To jest krok numer:", krok)
    #print("*")

for krok in range(12, 14):
    print("To jest krok numer:", krok)

for krok in range(11, 5, -1):
    print("To jest krok numer:", krok)

print()
for liczba in range(0, 11, 2):
    print(liczba)

#Poproś użytkownika o podanie liczby
#wyświetl tabliczkę mnożenia dla tej liczby do 10

#napisz symulator skarbonki
#podajemy 10 kwot wpłaty i na koniec wyświetlamy
#ile mamy pieniędzy w skarbonce

#*
#narysuj kwadrat z gwiazdek o boku podanym przez użytkownika

liczba = 5
linia = ""
for krok in range(liczba):
    linia = linia + " * "

for krok in range(liczba):
    print(linia)

liczba = ""
while liczba != "0":
    liczba = input("Podaj liczbę: ")

pesel = ""
while len(pesel) != 11:
    pesel = input("Podaj PESEL: ")
print("Dzięki za poprawny PESEL :)")

#zadanie 3 z "Ćwiczenia - pętle"
#później pozostałe :)