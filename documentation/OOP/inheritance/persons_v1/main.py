# Öröklődés
# parent (szülő/ősosztály) class
class Person(object):    
  
        # konstruktor         
        def __init__(self, name, idnumber):   
                self.name = name
                self.idnumber = idnumber

        def display(self):
                print(self.name)
                print(self.idnumber)
  
# child (gyermek/származtatott) class
class Employee(Person):           
        def __init__(self, name, idnumber, salary, post):
                self.salary = salary
                self.post = post
  
                # a szülő osztály konstruktorra is történik utalás 
                Person.__init__(self, name, idnumber) 
  

# A következő kódrészletek már az osztályokon kívül vannak                  
# objektum példányosítása
a = Employee('Sanyi', 886012, 200000, "Gyakornok")    
  
# az objektumhoz tartozó funkció meghívása
a.display() 
