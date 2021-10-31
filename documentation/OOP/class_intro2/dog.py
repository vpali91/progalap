# Osztály: Egy olyan tervrajzként érdemes felfogni, ami alapján az objektumokat "legyártjuk"
# Az osztályon belüli dolgok egy tabulátorral beljebb kerülnek

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
