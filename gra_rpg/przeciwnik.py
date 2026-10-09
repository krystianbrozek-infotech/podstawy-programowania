import random

class Przeciwnik:
    def __init__(self):
        self.imie = ""
        self.zdrowie = 10
        self.exp = random.randint(1, 5)
        self.sila = 5
        self.losujPrzeciwnika()

    def losujPrzeciwnika(self):
        przeciwnik = random.randint(1, 3)
        if przeciwnik == 1:
            self.imie = "Pikaczu"
            self.zdrowie += 5 #zdrowie = zdrowie + 5
        elif przeciwnik == 2:
            self.imie = "Czarodziej"
            self.zdrowie -= 2
            self.sila -= 1
        else:
            self.imie = "Smok"
            self.zdrowie += 10
            self.sila += 3

        przeciwnik = random.randint(1,4)
        if przeciwnik == 1:
            self.imie = "Straszliwy " + self.imie
            self.sila += 2
        elif przeciwnik == 2:
            self.imie = "Zły " + self.imie
            self.sila += 1
        elif przeciwnik == 3:
            self.imie = "Wielki " + self.imie
            self.zdrowie += 3
        else:
            self.imie = "Potężny " + self.imie

        przeciwnik = random.randint(1,2)
        if przeciwnik == 1:
            self.imie += " Zagłady"
            self.sila+= 5
        else:
            self.imie += " Zniszczenia"
            self.sila += 3

    def przedstawSie(self):
        print(f"Zaatakował Cię {self.imie}   HP: {self.zdrowie}   Siła: {self.sila}")