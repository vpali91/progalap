# parent class
class Person(object):    
      
        # konstruktor         
        def __init__(self, name, idnumber):   
                self.name = name
                self.idnumber = idnumber

        def display(self):
                print(self.name)
                print(self.idnumber)
