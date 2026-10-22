from aplikacja import Aplikacja

class Komputer:
    def __init__(self, ilePamieci):
        self.pamiec = ilePamieci
        self.zajetaPamiec = 0
        self.procesor = 0
        self.dyskPojemnosc = 512
        self.dyskZajetosc = 0
        self.bateria = 100
        self.dzialajacaApka = None

    def przedstawSie(self):
        return f"Komputer: pamięć: {self.zajetaPamiec}/{self.pamiec}" #...

    def uruchom(self, apka: Aplikacja):
        self.dzialajacaApka = apka
        self.zajetaPamiec += apka.zuzyciePamieci
        self.dyskZajetosc += apka.zajetoscDysku
        self.bateria -= apka.zuzycieBaterii

    def jakaApkaDziala(self):
        if self.dzialajacaApka == None:
            print("Nic nie jest uruchomione")
        else:
            print(f"Działa: {self.dzialajacaApka.nazwa}")

    