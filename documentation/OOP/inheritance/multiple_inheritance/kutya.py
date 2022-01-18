from emlos import Emlos
from uszas import Uszas
# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetetten az Allat osztályból származik az Emlős osztályon keresztül
class Kutya(Emlos, Uszas):
      
    # Constructor
    def __init__(self, nev, suly, kor, szorosseg, fajta, uszas_sebesseg,uszas_idotartam):
        Emlos.__init__(self,nev, suly, kor, szorosseg)
        Uszas.__init__(self,uszas_sebesseg,uszas_idotartam)
        self.fajta = fajta

    def ugat(self):
        print("Vau")
