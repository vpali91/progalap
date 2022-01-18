from madar import Madar
from repul import Repul
from uszas import Uszas

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetetten az ősosztálytól származik a Madar osztályon keresztül
class Kacsa(Madar,Repul,Uszas):
      
    # Constructor
    def __init__(self, nev, suly, kor, tollassag, sebesseg, idotartam, uszas_sebesseg, uszas_idotartam):
        Madar.__init__(self,nev, suly, kor, tollassag)
        Repul.__init__(self,sebesseg, idotartam)
        Uszas.__init__(self, uszas_sebesseg, uszas_idotartam)
  
    def hapog(self):
        print("Háp")
