# Ez a futtatható fájlunk, ahol az objektumokat példányosítjuk az osztályokból
# Ehhez importálnunk kell azokat az osztályokat, amikre hivatkozni kívánunk
# Formátum: from file_név import osztály_név
from cat import Cat
from dog import Dog

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
