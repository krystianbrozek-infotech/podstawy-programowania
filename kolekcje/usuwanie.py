lista = []
lista.append("Niebiesk")
lista.append("Zielony")
lista.append("Czerwony")
lista.append("Żółty")
lista.append("Zielony")

lista.remove("Zielony") #usuwa pierwszy element, który znajdzie
lista.pop(0) #usuwa element o wskazanym indeksie (numerze elementu)
#lista.clear() #czyści listę ze wszystkich elementów

for kolor in lista:
    print(kolor, end=", ")