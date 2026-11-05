osoby = []
imie = None

while imie!="":
    imie = input("Podaj imię: ")
    if imie != "":
        nazwisko = input("Podaj nazwisko: ")
        osoby.append(f"{imie} {nazwisko}")

print()
print("Lista mieszkańców:")



#usuwanie mieszkańców
usuwany = None
while usuwany != 0:
    #wyświetlenie wszystkich mieszkańców
    nr = 1
    for o in osoby:
        print(f"{nr}. {o}")
        nr+= 1
    #odczytujemy co chcemy usunąć (i zamieniamy na int)
    usuwany = int(input("Którego mieszkańca usunąć? "))
    if usuwany != 0:
        osoby.pop(usuwany-1) #usuwamy wskazany element

# nr = 0
# while nr < len(osoby):
#     print(osoby[nr])

#odczytuj liczby do momentu podania 0
#liczby zapisuj na liście
#na koniec wyświetl:
#   pierwszą podaną liczbę
#   sumę liczb
#   najmniejszą i największą liczbę
#*  wszystkie liczby po przecinku