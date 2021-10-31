# importálnunk kell a fájlt, amiben az osztályunk szerepel.
from NPC import NPC

# 3 objektum kerül jelen példában példányosításra, a zárójelben azok a paraméterek vannak, amit a konstruktor vár az osztályban
belethor = NPC("Belethor", "breton", 100, False)
sheogorath = NPC("Sheogorath", "daedric", 100, True)
maiq = NPC("M'aiq the Liar", "khajiit", 100, True)

# hivatkozhatunk az objektumok attributumaira, vagy funkcióira
belethor.speak()

belethor.injured(30)
print(belethor.hp)
belethor.heal(40)
print(belethor.hp)

