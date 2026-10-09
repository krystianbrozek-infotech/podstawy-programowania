class Osoba:
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.PESEL = ""

    def przedstaw_sie(self):
        return f"Nazywam się {self.imie} {self.nazwisko}, mój PESEL to {self.PESEL}."    