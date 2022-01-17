from allat import Allat

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetlenül az ősosztálytól származik és az ebből leszármazó osztálynak a szülő/parent osztálya
class Emlos(Allat):
      
    # Constructor
    def __init__(self, nev, suly, kor, szorosseg):
        Allat.__init__(self,nev, suly, kor)
        self.szor_hossz = szorosseg
  
    def szor_novekszik(self):
        self.szor_hossz += 1

    def vedlik(self):
        self.szor_hossz -= 1

    def harap(self):
        print("Megharaplak")
