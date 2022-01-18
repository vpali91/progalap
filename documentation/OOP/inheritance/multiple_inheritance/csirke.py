from madar import Madar
from repul import Repul

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetetten az ősosztálytól származik a Madar osztályon keresztül
class Csirke(Madar,Repul):
      
    # Constructor
    def __init__(self, nev, suly, kor, tollassag, tartas, sebesseg, idotartam):
        Madar.__init__(self,nev, suly, kor, tollassag)
        Repul.__init__(self,sebesseg, idotartam)
        self.tartas = tartas
  
    def kotkodacsol(self):
        print("Kot ko dács!")
