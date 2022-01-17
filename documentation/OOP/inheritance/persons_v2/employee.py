from person import Person
# child class
class Employee(Person):           
        def __init__(self, name, idnumber, salary, post):
                self.salary = salary
                self.post = post
  
                # a szülő osztály konstruktorra is történik utalás 
                Person.__init__(self, name, idnumber) 
  
