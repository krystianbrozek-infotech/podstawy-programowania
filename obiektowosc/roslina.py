class Roslina:
    def __init__(self):
        self.kolor = "zielony"
        self.nazwa = ""
        self.wysokoscMM = 100
        self.maxWodyML = 50
        self.maxWzrostMM = 1

    def podlej(self, ileWodyML):
        if self.maxWodyML < ileWodyML:
            ileWodyML = self.maxWodyML
        wzrost = (self.maxWzrostMM / self.maxWodyML) * ileWodyML
        self.wysokoscMM += wzrost

    def przedstawSie(self):
        print(f"Jestem {self.nazwa} i mam {self.wysokoscMM}mm wysokości <3")

    def nawoz(self, ileG):
        self.wysokoscMM += ileG

    def nawoz2(self, ileG):
        if ileG > 10:
            ileG -= 10
            self.wysokoscMM -= ileG
        else:
            #self.wysokoscMM += ileG
            self.nawoz(ileG)

#1. przedstawianie się
#2. nawóz - za każdy gram nawozu roślina rośnie o 1mm
#3. nawóz - jak damy więcej niż 10g nawozu, 
#           to roślina traci 1mm za każdy gram ponad 10g nawozu