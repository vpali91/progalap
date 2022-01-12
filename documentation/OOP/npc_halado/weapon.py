class Weapon:
    def __init__(self,nev, sebzes):
        self.name = nev
        self.damage = sebzes
        self.hp = 100

    def self_damage(self):
        self.hp -=1
