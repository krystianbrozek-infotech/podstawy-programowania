class Bron:
    def __init__(self, nazwa, cena, obrazenia, amunicja):
        self.amunicja = amunicja
        self.obrazenia = obrazenia
        self.nazwa = nazwa
        self.cena = cena
        self.czyDystansowa = amunicja > 0

    def przedstawSie(self):
        return f"{self.nazwa}  {self.cena}GD"
