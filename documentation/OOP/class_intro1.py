# Osztály: Egy olyan tervrajzként érdemes felfogni, ami alapján az objektumokat "legyártjuk"
# Az osztályon belüli dolgok egy tabulátorral beljebb kerülnek

#Osztály paraméterek nélkül, ilyenkor csak azonos tulajdonságokkal hozhatjuk létre az objektumot, hiszen nincs konstruktorunk, ami paramétert várna
class Cat:
    # az osztály attributumai (tulajdonságai), ezek általában változók, vagy objektumok is lehetnek másik osztályból létrehozva(itt most ez utóbbi nincs)
    name = "Cirmi"
    age = 3
    weight = 5
    is_alive = True

    # funkció, a self nem paraméter, hanem csak arra utal, hogy az osztályon belül van, a paramétereket mellé lehet írni vesszővel elválasztva
    def kill(self):
        self.is_alive = False

    def eat(self, kaja):
        self.weight += kaja

    def aging(self):
        self.age += 1

    def karmol(self):
        print("Karmol")

# Osztály, ami paramétereket vár
class Dog:
    # Konstruktor: hasonló a funckiókhoz, de nem az. Itt adhatunk paramétereket az objektumunknak létrejöttekor, így több meghívással különféle értékeket adhatunk a tulajdonságoknak
    # A self kötelező tartalmi elem, de nincs jelentősége, vesszővel elválasztva utána a paraméterek
    def __init__(self, nev, eletkor, suly, elo):
        self.name = nev
        self.age = eletkor
        self.weight = suly
        self.is_alive = elo
    
    def kill(self):
        self.is_alive = False

    def eat(self, kaja):
        self.weight += kaja

    def aging(self):
        self.age += 1

    def ugat(self):
        print("Vau")

# Objektum példányosítása(létrehozása):
# objektum_neve = Cat()  --> Cat() az osztály neve, ami alapján legyártjuk az objektumot
cirmi = Cat()

# cirmi néven létrejött egy objektumunk, ez addig a memóriában él, amíg fut a program, vagy nem töröljük
# Innentől kezdve meghívhatjuk funkcióit és lekérhetjük, módosíthatjuk tulajdonságait.

# objektum_nev.tulajdonság, így hívhatjuk meg az osztály attributumait
print(f" cirmi tulajdonságai: nev: {cirmi.name} kor: {cirmi.age}, suly: {cirmi.weight}, életben van:{cirmi.is_alive}")

# Tudjuk módosítani az attributumokat is:
cirmi.name = "Cirmii"

# objektum_név.funkció_név(), így hívhatjuk meg az osztály funkcióit
cirmi.eat(2)
print(f" cirmi tulajdonságai: nev: {cirmi.name} kor: {cirmi.age}, suly: {cirmi.weight}, életben van:{cirmi.is_alive}")

cirmi.aging()
print(f" cirmi tulajdonságai: nev: {cirmi.name} kor: {cirmi.age}, suly: {cirmi.weight}, életben van:{cirmi.is_alive}")

cirmi.karmol()
cirmi.kill()
print(f" cirmi tulajdonságai: nev: {cirmi.name} kor: {cirmi.age}, suly: {cirmi.weight}, életben van:{cirmi.is_alive}")

# Objektum létrehozása paraméterekkel
# Itt látszik leginkább miért hasznosak az objektumok, egy osztályt írtunk meg és 3 objektumot hozunk létre belőle
# Ezek mind a memóriában élnek egymástól függetlenül a paramétereik szerint
bundas = Dog("Bundás",6,10,True)
bodri = Dog("Bodri", 10,20,True)
zombi = Dog("Aaargh",30,15,False)
print(f" {bundas.name} tulajdonságai: kor: {bundas.age}, suly: {bundas.weight}, életben van:{bundas.is_alive}")

print(f" {bodri.name} tulajdonságai: kor: {bodri.age}, suly: {bodri.weight}, életben van:{bodri.is_alive}")

print(f" {zombi.name} tulajdonságai: kor: {zombi.age}, suly: {zombi.weight}, életben van:{zombi.is_alive}")
