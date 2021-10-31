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
        global is_alive
        is_alive = False

    def eat(self, kaja):
        self.weight += kaja

    def aging(self):
        self.age += 1

    def karmol(self):
        print("Karmol")
