# Mindig be kell importálni random-ot, ha használni szeretnéd
import random

lista = ['banana', 'apple', 'strawberry', 'blackberry']
# random.randint(szam1, szam2) szam1-szam2-ig kigenerál egy random számot
print(random.randint(1, 10))

# random.random() - kigenerál egy float számot, nulla egész valamennyi
print(random.random())

# random.choice(lista) - Kiválaszt random 1 elemet a listából
print(random.choice(lista))

# random.choice(lista,k=darab) - Kiválaszt random x darab elemet a listából
print(random.choices(lista,k=2))

# random.shuffle(lista) - Összekeveri a lista elemeit
random.shuffle(lista)
print(lista)
