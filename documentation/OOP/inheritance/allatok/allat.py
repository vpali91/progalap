# Ősosztály, angolul: Base or Super class.
# Ez lesz a példában minden osztály őse
class Allat(object):
      
    # konstruktor
    def __init__(self, nev, suly, kor):
        self.nev = nev
        self.suly = suly
        self.kor = kor
        self.el = True
  
    def meghal(self):
        self.el = False

    def eszik(self, kaja):
        self.suly += kaja
