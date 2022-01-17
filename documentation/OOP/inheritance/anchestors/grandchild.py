from child import Child

# Származtatott osztály, angolul: Inherited or Sub class
# Ez az osztály közvetetten a Child szülő osztályon keresztül származik le a Base ősosztályból
# Ez az osztály a Child osztály változóit és funkcióit örökli, viszont a Child osztály a Base osztálytól örökölte ezek egy részét
class GrandChild(Child):
      
    # konstruktor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
 
    def getAddress(self):
        return self.address
