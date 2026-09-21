x = 3
if x > 0:
    print("Dodatnia")
elif x == 0:
    print("Zero")
elif x == 3:
    print("Lubię 3")
else:
    print("Ujemna")

PESEL = "02321188904"
cyfra = PESEL[9]
liczba = int(cyfra)

if liczba % 2 == 0:
    print("Jesteś kobietą")
else:
    print("Jesteś mężczyzną")

#1. odczytaj od użytkownika 2 liczby i napisz która z nich jest większa
#2. poproś użytkownika o wiek i powiedz czy jest pełnoletni
#3. 