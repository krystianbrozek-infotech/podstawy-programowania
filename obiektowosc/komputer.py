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
        if self.pamiec + apka.zuzyciePamieci > self.zajetaPamiec: return False
        if self.dyskZajetosc + apka.zajetoscDysku > self.dyskPojemnosc: return False
        if self.bateria < apka.zuzycieBaterii: return False
        if self.procesor + apka.zuzycieProcka > 100: return False

        self.dzialajacaApka = apka
        self.zajetaPamiec += apka.zuzyciePamieci
        self.dyskZajetosc += apka.zajetoscDysku
        self.bateria -= apka.zuzycieBaterii
        self.procesor += apka.zuzycieProcka
        return True

    def zamknijAplikacje(self):
        # if self.dzialajacaApka != None:
        #     self.procesor -= self.dzialajacaApka.zuzycieProcka
        #     self.dyskZajetosc -= self.dzialajacaApka.zajetoscDysku
        #     self.zajetaPamiec -= self.zajetaPamiec
        #     self.dzialajacaApka = None

        if self.dzialajacaApka == None: return

        self.procesor -= self.dzialajacaApka.zuzycieProcka
        self.dyskZajetosc -= self.dzialajacaApka.zajetoscDysku
        self.zajetaPamiec -= self.zajetaPamiec
        self.dzialajacaApka = None


    def jakaApkaDziala(self):
        if self.dzialajacaApka == None:
            print("Nic nie jest uruchomione")
        else:
            print(f"Działa: {self.dzialajacaApka.przedstawSie()}")

    def restart(self):
        self.dzialajacaApka = None
        self.zajetaPamiec = 0
        self.dyskZajetosc = 0
        self.procesor = 0

    def ladujBaterie(self):
        self.bateria = 100

    