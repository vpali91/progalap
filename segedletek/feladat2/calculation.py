class Calculation:
    def __init__(self, ber):
        self.netto = ber
        self.diak = 0
        self.rendes_mv = 0

    def szamolas(self):
        self.diak = self.netto*1.15
        self.rendes_mv = self.netto*1.83
