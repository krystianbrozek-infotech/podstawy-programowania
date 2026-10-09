import osoba

czlowiek = osoba.Osoba()
czlowiek.imie = "Jan"
czlowiek.nazwisko = "Nowak"
czlowiek.PESEL = "12345678901"

ludzik = osoba.Osoba()
ludzik.imie = "Anna"
ludzik.nazwisko = "Kowalska"
ludzik.PESEL = "98765432109"

print(czlowiek.przedstaw_sie())
print(ludzik.przedstaw_sie())