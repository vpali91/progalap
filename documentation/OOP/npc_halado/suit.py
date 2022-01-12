class Suit:
    def __init__(self, nev, vedelem):
        self.name = nev
        self.defense = vedelem

    def damaged(self, damage):
        self.defense -= damage*0.5
