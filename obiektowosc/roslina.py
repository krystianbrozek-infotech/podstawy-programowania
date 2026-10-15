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