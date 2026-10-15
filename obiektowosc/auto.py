class Auto:
    def __init__(self):
        self.moc = 100
        self.marka = "Toyota"
        self.waga = 1500
        self.predkoscMax = 200
        self.kolor = "biały"
        self.pojBaku = 30
        self.paliwo = 10
        self.przebieg = 0

    def stanBaku(self):
        print(f"Stan baku: {self.paliwo}/{self.pojBaku} litrów")

    def zatankuj(self, ile):
        self.paliwo += ile
        if self.paliwo > self.pojBaku:
            self.paliwo = self.pojBaku

    def zatankuj2(self, ile):
        if self.paliwo + ile > self.pojBaku:
            ile = self.pojBaku - self.paliwo
        self.paliwo += ile

    def jedz(self, ile):
        spalanie = ile / 100.0 * 10
        if spalanie <= self.paliwo:
            self.przebieg += ile
            self.paliwo -= spalanie
            return True
        return False
        