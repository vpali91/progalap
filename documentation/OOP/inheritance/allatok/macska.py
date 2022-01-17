from emlos import Emlos

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetetten az Allat osztályból származik az Emlős osztályon keresztül
class Macska(Emlos):
      
    # Constructor
    def __init__(self, nev, suly, kor, szorosseg, fajta):
        Emlos.__init__(self,nev, suly, kor, szorosseg)
        self.fajta = fajta

    def nyavog(self):
        print("Meow")

    def karmol(self):
        print("Megkarmoltalak")
    
