def przywiatnie(imie):
    print("Witaj", imie, "!")
    print("--------------------")

def pokazWieksza(liczba):
    print(liczba+2)

def pokazWieksza2(liczba):
    return liczba+2

def siemka(imie, nazwisko):
    print("Siemanko", imie, nazwisko, "!")

def siemka2(imie, nazwisko):
    return f"Siemanko {imie} {nazwisko}!"

def szescian(liczba):
    return liczba*liczba*liczba

def sprawdz(a, b):
    if a == 0:
        return False
    if b == 0:
        return False
    if a < 0 and b < 0:
        return False
    return True

a = 0
b = 0
if a != 0 and b != 0 and (a < 0 or b < 0):
    print("Wszystko jest ok")

if sprawdz(1, 2):
    print("Wszystko jest ok")

wynik = pokazWieksza2(5)
print(wynik)

przywitanie = siemka2("Jan", "Kowalski")
print(przywitanie)

# przywiatnie("Jan")
# imie = input("Podaj swoje imię: ")
# przywiatnie(imie)

# pokazWieksza(5)
# x = int(input("Podaj liczbę: "))
# pokazWieksza(x)

#stwórz funkcję, która służy do odczytania liczby
#funkcja powinna przyjmować parametr, który będzie komunikatem do wyświetlenia dla użytkownika
#w zamian zwraca liczbę w postaci int

def odczytajLiczbe(komunikat):
    liczba = int(input(f"{komunikat}: "))
    return liczba

liczba1 = odczytajLiczbe("Podaj liczbę")
liczba2 = odczytajLiczbe("Podaj drugą liczbę")