from suit import Suit
from weapon import Weapon

class NPC:
    def __init__(self, nev, elet, baratsagos):
        self.name = nev
        self.hp = elet
        self.friendly = baratsagos
        self.ebony = Suit("Ebony", 90)
        self.primary = Weapon("Blade", 15)
        self.secondary = Weapon("Knife", 3)
    
    def injuring(self,damage):
        self.hp -= (damage-(damage*(self.ebony.defense/100)))
        self.ebony.damaged(damage)

    def healing(self):
        self.hp += 10

    def attack(self, weapon_number):
        if weapon_number == 1:
            self.primary.self_damage()
            return self.primary.hp
        else:
            self.secondary.self_damage()
            return self.secondary.hp
