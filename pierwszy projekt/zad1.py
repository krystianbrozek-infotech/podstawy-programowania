#odczytaj imię od użytkownika i przywitaj się z nim
imie = input("Jak masz na imię? ")
print(f"Witaj {imie}! Milutko Cię widzieć :)")

#odczytaj liczbę od użytkownika i wyświetl ją o dwa większą
liczba = int(input("Podaj liczbę: "))
print(f"Twoja powiększona liczba {liczba+2}")

#1. Odczytaj od gracza ulubiony kolor...
kolor = input("Jaki jest Twój ulubiony kolor? ")
zwierze = input("Jakie jest Twoje ulubione zwierze? ")
print(f"Twój nowy super nick: {kolor}_{zwierze}_PL")

#2 nick z discorda
nick = input("Podaj swój nick z Discorda: ")
rozlozony_nick = nick.split("#")
print(f"Witaj na serwerze, {rozlozony_nick[0]}")

#3 liczba godzin
godziny = int(input("Ile godzin spędziłeś w grze? "))
dni = godziny // 24
reszta = godziny % 24
print(f"Grałeś {dni} dni i {reszta} godzin")