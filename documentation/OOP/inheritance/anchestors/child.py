from base import Base

# Származtatott osztály: Inherited or Sub class
# Példánkban ez az osztály közvetlenül az ősosztálytól származik és az ebből leszármazó osztálynak a szülő/parent osztálya
class Child(Base):
      
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
  
    def getAge(self):
        return self.age
