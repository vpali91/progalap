import random
# Osztály: Egy olyan tervrajzként érdemes felfogni, ami alapján az objektumokat "legyártjuk"
# Az osztályon belüli dolgok egy tabulátorral beljebb kerülnek

# Osztály, ami paramétereket vár
class NPC:
    # Konstruktor: hasonló a funckiókhoz, de nem az. Itt adhatunk paramétereket az objektumunknak létrejöttekor, így több meghívással különféle értékeket adhatunk a tulajdonságoknak
    # A self kötelező tartalmi elem, de nincs jelentősége, vesszővel elválasztva utána a paraméterek
    def __init__(self, nev, faj, elet, halhatatlan):
        self.name = nev
        self.race = faj
        self.hp = elet
        # mivel a halhatatlan érték még string, ezt bool értékre kell konvertálnunk
        def immortalise(halhatatlan):
            if halhatatlan=="True":
                return True
            elif halhatatlan=="False":
                return False
        # értékadásnál meghívjuk az immortalise() funkciót, ami logikai értékkel tér vissza
        self.immortal = immortalise(halhatatlan)
    
    def speak(self):
        #Lokális lista, amit csak ezen funckión belül érünk el
        quotes = ["I used to be an adventurer like you. Then I took an arrow in the knee.", "Never should have come here!", "Let me guess… someone stole your sweetroll?"]
        # lokális változó, amit csak ezen a funkción belül érünk el 
        rnd = random.randint(0,2)
        print(quotes[rnd])

    def injured(self, damage):
        # globális változóra hivatkozunk self.hp, míg a damage paraméterünk lokális változó
        self.hp -= damage

    def heal(self, healing):
        self.hp += healing
