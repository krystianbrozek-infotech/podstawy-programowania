lista = [1, 2, 3]
lista[1]
krotka = (1, 2, 3) #tuple
krotka[1]
zbior = {1, 2, 3}
#nie ma odwołania po indeksie
slownik = {"a": 50, "b": 70, "c": 4}
slownik["a"]
parametryLudzia = {"imie": "Krystian", "nazwisko": "Brożek"}
parametryLudzia["wiek"] = 67
print(parametryLudzia["wiek"])
slownikUdajacyListe = {0: "Lubię placki", 1: "Gram w GTA", 2: "noszę spodnie, ale nie zawsze"}

#1. 
for e in lista:
    print(e)

listaWykladow = {"Wykład 1": "Dokąd tupta nocą jeż"}
listaWyk = {"Dokąd tupta nocą jeż": object}

#zad1: książka telefoniczna. Zapisz w wybranej kolekcji numery telefonów:
#Ewa 510123123, Jola 633331331, Jan 500300100, Ula 880100100
#zad1.1: wybierz numer Ewy i go wyświetl
