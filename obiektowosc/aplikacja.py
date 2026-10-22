import random

class Aplikacja:
    def __init__(self, nazwa, pamiec, dysk, bateria):
        self.zuzyciePamieci = pamiec
        self.zajetoscDysku = dysk
        self.nazwa = nazwa
        self.zuzycieBaterii = bateria
        self.zuzycieProcka = random.randint(10,13)

    def przedstawSie(self):
        return f"{self.nazwa}  pamięć: {self.zuzyciePamieci}  dysk: {self.zajetoscDysku}"