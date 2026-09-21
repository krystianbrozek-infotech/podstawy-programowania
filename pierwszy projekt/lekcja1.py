#deklaracja zmiennej
x = 5
#str - tekst, 
#bool - wartość logiczna (True/False), 
#int - l. całkowita, 
#float - l. dziesiętna
y: float = 10.5
z = x + y
z = z + 3
z += 3
z *= 2 #z = z*2
z = 10 / 2
z = 9 // 2 #dzielenie całkowito liczbowe
print(z)
print(9 % 2) #% to modulo, czyli reszta z dzielenia

liczba = input("Podaj mnie liczbę: ")
naprawde_liczba = int(liczba) #funkcja int zamienia tekst na liczbę całkowitą
print(naprawde_liczba % 3)
print(liczba, "lubię placki", "ala ma kota", z)

imie = "Krystian"
nazwisko = "Krystiaonowy"
przywitanie = f"Witaj {imie} {nazwisko}!{z}"
przywitanie = "Witaj " + imie + " " + nazwisko + "!" + str(z)
print(przywitanie)
print()
str(123) 
int("123")
float("123.23")
napis = "lubię placki, ponieważ są dobre. Znam przepis na placki, ale słabo mi wychodzą"
slowa = napis.split(" ")
print(slowa[0])
print(napis[0])
print(napis.replace("placki", "naleśniki"))
print(napis.replace("ż", "z").replace("ę", "e"))
dlugosc = len("napis")
print(dlugosc)