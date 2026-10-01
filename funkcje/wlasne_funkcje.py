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
