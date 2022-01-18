from emlos import Emlos
from madar import Madar

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetetten az ősosztálytól származik a Madar osztályon keresztül
class KacsacsoruEmlos(Madar,Emlos):
      
    # Constructor
    def __init__(self, nev, suly, kor, tollassag,szorosseg):
        Madar.__init__(self,nev, suly, kor, tollassag)
        Emlos.__init__(self,nev, suly,kor, szorosseg)

    def sardagaszt(self):
        print("Sárt dagasztok")
  
