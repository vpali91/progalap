from turtle import Turtle, Screen, showturtle

# A screen object metódusokról a screen_methods.py-ban lesz szó

# név = Turtle() Létrejön a turtle objektumunk a Turtle beépített osztályból
# Ez tartalmazza a grafikus dolgokat ami az ablakon belül történik
bob = Turtle()

# screen = Screen() Létrejön a screen objektumunk a Screen beépített osztályból
# Ez lesz az ablaka a grafikus felületünknek 
screen = Screen()

# Itt adunk egy formát annak a objektumnak, amit mozgatunk  pl: ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’
bob.shape("turtle")

# Itt adunk egy színt a mozgatott objektumnak, ezzel fog rajzolni is
bob.color("red")

# objektum_név.forward(távolság) --> a grafikus objektumunk mennyit mozogjon előre
bob.forward(50)

# objektum_név.right(szög) --> a grafikus objektumunk mennyit forduljon jobbra
bob.right(90)

# objektum_név.backward(távolság) --> a grafikus objektumunk mennyit mozogjon hátra
bob.backward(50)

# objektum_név.left(szög) --> a grafikus objektumunk mennyit forduljon balra
bob.left(42)
bob.forward(50)

# objektum_név.stamp() --> hagy egy lenyomatot az éppen aktuális alajáról a grafikus objektumunk
bob.stamp()

# objektum_név.penup() --> a grafikus objektumunk nem rajzol tovább
bob.penup()
bob.forward(50)

# objektum_név.pendown() --> a grafikus objektumunk újra rajzol
bob.pendown()
bob.forward(50)

# Zárt sokszögek esetén használhatjuk a fill parancsot, ezzel kitöltjük színnel a belsejét
# Kitöltő szín meghatározása
bob.fillcolor("red")
# kitöltés megkezdése, amint kész az alakzat, kitöltésre kerül
bob.begin_fill()
for _ in range(4):
    bob.forward(100)
    bob.right(90)
# kitöltés befejezése
bob.end_fill()

# objektum_név.clear() --> törlődik minden rajzunk az ablakból
bob.clear()
bob.penup()

# objektum_név.() --> a grafikus objektumunk visszakerül a kiindulási helyére (penuppal használjuk, különben húz egy csíkot a végpont és a kiindulási pont között)
bob.home()
bob.pendown()

# objektum_név.circle(radius) --> a grafikus objektumunk kört rajzol a megadott sugárral
bob.circle(50)

# objektum_név.goto(x,y) --> a grafikus objektumunk a megadott koordinátára kerül, 0,0 kiindulási pont (bob.home())
bob.goto(50,50)

# objektum_név.setheading(szög) --> a grafikus objektumunk elfordul a megadott szögben
bob.setheading(30)

# objektum_név.speed(szám) --> a grafikus objektumunk animációjának sebességét adja meg 1-10-es skálán (6 a normál, 0 az áttűnés)
bob.speed(1)
bob.forward(200)

# objektum_név.distance(x,y) -->  a grafikus objektumunk távolságát adja meg az adott koordinátától
print(bob.distance(0,0))

# objektum_név.ycor() -->  a grafikus objektumunk y koordinátáját adja meg
print(bob.ycor())

# objektum_név.xcor() -->  a grafikus objektumunk y koordinátáját adja meg
print(bob.xcor())

# A rajzoláson számos dolgot állíthatunk még, ha több paramétert adunk meg a zárójelben
bob.pen(fillcolor="black", pencolor="red", pensize=10)

# így is megadhatjuk a toll vastagságát
bob.pensize(5)

# Elrejthetjük objektumunkat, ettől még ott van.
bob.hideturtle()
bob.forward(100)

# Láthatóvá is tehetjük
bob.showturtle()

# screen_objektum.exitonclick(), ha ezt kihagyod, akkor amint lefutott a programunk, azonnal kilépne az ablakunkból
# ennek segítségével nyitva marad az ablakunk a rajzolás végén is, kattintással zárhatjuk be az ablakunkat
screen.exitonclick()

# Ezen az oldalon találhatsz példákat rajzolásra:
# https://www.geeksforgeeks.org/turtle-programming-python/

# A doksi nem teljes, a teljes turtle dokumentációt itt találod számos más paranccsal: https://docs.python.org/3/library/turtle.html
