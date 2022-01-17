# Ősosztály, angolul: Base or Super class.
# Ez lesz a példában minden osztály őse
class Base(object):
      
    # konstruktor
    def __init__(self, name):
        self.name = name
  
    def getName(self):
        return self.name
