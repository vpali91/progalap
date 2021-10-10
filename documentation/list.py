import random
#List pythonban a listák nincsenek típushoz kötve, tárolhatsz különféle típusú változókat egy listában
# pythonban nem kell megadni a lista hosszát sem, ha nem adunk meg értékeket

lista1 = [3,6,2,9,5,7,3]
lista2 = ["banana", "apple", "peach", "strawberry"]
lista3 = [1, "banana", True, 1.5]
lista4 = []

# hozzádás a listához
# lista.append(érték)
lista4.append("asd")
print(lista4)

# meglévő elem felülírása listán belül
lista1[1]=10

# lista elemeinek megszámolása: len(lista)
print(len(lista1))

# lista.count(keresett) - megszámolja adott elemre az összes találatot
print(lista1.count(3))

# lista kiterjesztése lista1.extend(lista2) - lista1-hez hozzáadjuk lista2 elemeit
lista3.extend(lista2)
print(lista3)

# lista.insert(index, érték): elem hozzáadása a listához az indexnek megfelelő helyre, nem írja felül az azon a helyen álló értéket, hanem előrébb tolja 1-el
lista1.insert(1,100)
print(lista1)

# lista.remove(érték): eltávolítja az első találatot a megadott értékből a listából (a 2. ugyanilyen elem már ott marad, while-al kombinálhatod)
lista1.remove(3)
print(lista1)

# lista.sort(): növekvő sorrendbe teszi a lista elemeit, számot és stringet is akár.
lista1.sort()
print(lista1)
lista2.sort()
print(lista2)

# random.shuffle(lista): összekeveri a lista elemeit random módon
random.shuffle(lista1)
print(lista1)

# lista.reverse(): megfordítja a sorrendet a listában. !!!Nem csökkenő sorrend!!!
# Ha csökkenő sorrendet szeretnél, először lista.sort() utána lista.reverse()
lista1.reverse()
print(lista1)

# lista kiíratása. pythonban akár iteráció nélkül is ki tudod írni a lista elemeit, amit más programnyelvnél nem tehetsz meg
print(lista1)

#egy adott elem kiíratása: 
print(lista1[1])

# kiíratás iterációval (pl for/while), más programnyelvnél ez a foreach-nek felel meg
for x in lista1:
    print(x)

#Kiíratás egy sorba szintén iterációval
print("Tömb elemei: ", end =" ")
for i in range(4):
    print(lista1[i], end = ", ")
