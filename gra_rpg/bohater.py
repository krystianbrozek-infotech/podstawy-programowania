class Bohater:
    def __init__(self, imie):
        self.imie = imie
        self.zdrowie = 20
        self.maxZdrowie = 20
        self.kasa = 0
        self.doswiadczenie = 0
        self.poziom = 1

    def przedstawSie(self):
        print(f"{self.imie}   HP: {self.zdrowie}/{self.maxZdrowie}   Kasa: {self.kasa}   Doświadczenie: {self.doswiadczenie}/50   Poziom: {self.poziom}")