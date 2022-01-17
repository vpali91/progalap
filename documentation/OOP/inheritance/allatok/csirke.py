from madar import Madar

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetetten az ősosztálytól származik a Madar osztályon keresztül
class Csirke(Madar):
      
    # Constructor
    def __init__(self, nev, suly, kor, tollassag, tartas):
        Madar.__init__(self,nev, suly, kor, tollassag)
        self.tollassag = tollassag
        self.tartas = tartas
  
    def kotkodacsol(self):
        print("Kot ko dács!")
