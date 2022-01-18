from allat import Allat

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetlenül az ősosztálytól származik és az ebből leszármazó osztálynak a szülő/parent osztálya
class Madar(Allat):
      
    # Constructor
    def __init__(self, nev, suly, kor, tollassag):
        Allat.__init__(self,nev, suly, kor)
        self.tollassag = tollassag
  
    def toll_ritkul(self):
        self.tollassag -= 1

    def tojik(self):
        self.suly -= 1

    def csip(self):
        print("Megcsiplek")
