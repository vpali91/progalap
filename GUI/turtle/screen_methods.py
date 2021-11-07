from turtle import Turtle, Screen, screensize

# objektum létrehozása a Turtle osztályból, ez felel az ablakon belüli dolgokért
tim = Turtle()
# objektum létrehozása a Screen osztályból, ez felel az ablakunkért és az interakciókért
screen = Screen()

# screen.title("Cím") --> A címsornak adhatunk címet
screen.title("Screen metódusok")

# screen.screensize(szám1, szám2) --> Az ablakon belüli tartalom méretét állítja be, nem az ablakméretet
screen.screensize(1000, 1000)

# screen.setup(szám1, szám2) --> Az ablak méretét állítja be
screen.setup(400,400)

# screen.bgcolor("szín") --> Háttérszínt ad az ablaknak
screen.bgcolor("yellow")

# változó_név = screen.textinput("Cím", "Utasítás szöveg")
input = screen.textinput("Inputbekérés", "Adj meg valamit")
print(input)
#screen.bgcolor(input)
#Kiíratás grafikus felületen, oda kerül, ahol éppen van a graf objektum. Elég csak a szöveget megadni, de több paramétert is meg lehet adni
tim.penup()
tim.goto(-100, 200)
tim.pendown()
tim.write(input, align="center", font=("Courier", 70, "normal"))

# változó_név = screen.numinput("Cím", "Utasítás szöveg", alapértelmezett_érték, minval=1, maxval=1000) input számbekérés min és max értékintervallum megadásával
numinput = screen.numinput("Számbekérés", "Adj meg egy számot", 10, minval=1, maxval=1000)

# 3 funkció, amelyek az előremenet és a fordulásért felelnek
def move_forward():
    tim.forward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

# funkció, ami törli a rajzot és visszahelyezi a kiindulási pontra a grafikus objektumunkat
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# screen.listen() --> "hallgatózik", figyeli az eseményeket, pl gombnyomás, egérműveletek, stb...
screen.listen()

#screen.onkey(funkcio_név_zárójel nélkül, "gomb") --> A megadott gombnyomásra a megadott funkció fut le és érzékeli a nyomvatartást
screen.onkeypress(move_forward, "w")
#screen.onkey(funkcio_név_zárójel nélkül, "gomb") --> A megadott gombnyomásra a megadott funkció fut le, nem érzékeli a nyomvatartást
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.exitonclick()

# További screen-el kapcsolatos content: https://docs.python.org/3/library/turtle.html#methods-of-turtlescreen-screen-and-corresponding-functions
