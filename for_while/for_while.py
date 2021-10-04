# Iterations/iterációk
# az iteráció fontos eleme a programozásnak, def: valamely eljárás ismétlődő végrehajtása
# iteráció esetén mindig a te felelősséged gondoskodni a program leállásáról, hogy ne legyen végtelen ciklus
# az önhívó rekurzió is az iterációk speciális esete, ezeket majd külön tárgyaljuk

#For loop/ for ciklus
# számolás 0-tól a megadott számig. Fontos: az utolsó számot már nem fogja kiírni és ebben az esetben 0-ról indul
for i in range(3):
    print(i)

# így adhatsz meg kezdőértéket
for i in range(1,3):
    print(i)

# for ciklus visszafelé
for i in reversed(range(6)):
    print(f"Visszaszámlálás: {i}")

# for ciklus léptetése több szám kihagyásával: pl, 2-esével
for i in range(1,10,2):
    print(f"kettesével: {i}")

# for loop-ok egymásba ágyazva
# A külső ciklus 5x fut le, a belső ciklus minden körben 6x
# Amikor lefut egy külső ciklus, azon belül 6 belső ciklus fut le
# pl: a külső ciklus 0. körében kiírja a számokat a belső ciklus 10-15-ig, utána az 1. körben ismételten...
# egymásba ágyazott ciklusoknál figyeljünk oda arra, hogy nem adhatjuk ugyanazt a változónevet a cikluson belül. Ha i van a külső ciklusban, akkor azt már nem adhatjuk meg a belső for ciklusba is, hivatkozni a kiíratásnál lehetne rá
for i in range(5):
    print(f"{i}.ciklus(i): ", end=" ")
    for j in range(10,16):
        print(j, end=", ")
    print("\n")

# string bontás for ciklussal:
txt = "Hello World"
for x in txt:
    print(x)

# lista kiíratása for ciklussal
lista1 = [3,6,2,9,5,7,3]

#kiíratás 0. elemtől
for x in lista1:
    print(x)

#kiíratás tetszőleges elemtől:
for i in range(2,4):
    print(lista1[i])

# else a for ciklus végén: megadhatjuk, hogy történjen-e valami miután kilép a program  a for ciklusból
print("lista kiíratása 2-5. elemig")
for i in range(2,6):
    print(lista1[i])
else:
    print("Vége")

# While
# while-t ugyanazokban az esetekben is tudjuk használni, mint a for ciklust, de annál specifikusabb esetekben is
# a while nagy előnye az erőforrás barát használati lehetőség(erre később lesz példa)
# while mindaddig lefut, amíg igaz a feltételünk, de abban az esetben el sem indul, ha a kezdetekben sem igaz a megadott feltétel
a = 0
nincs_vege = True
while nincs_vege:
    print(f"Nincs vége({a}. kör)")
    a+=1  # ha ez lemaradna végtelen ciklus lenne
    # Ha a == 5, akkor szeretnénk, hogy leálljon a while, ezért nincs_vege értékét átírjuk False-ra
    # Ezt követően mielőtt while lefutna, ellenőrzi nincs_vege értékét, észleli hogy false, így leáll, mielőtt újra lefutna
    if a==5:
        nincs_vege = False

#ugyanez így is működik:
b = 0
while b != 5:
    print(f"Megint nincs vége({b}. kör)")
    b+=1

#keresés while-al: ha van találat írja ki hogy van találat, nem kell végigfutnia
nincs_talalat = True
keresett =3
kor = 0
while nincs_talalat or kor<len(lista1):
    print(f"while, keresem {kor}. kör")
    if lista1[kor]==keresett :
        print("Van találat: ")
        nincs_talalat = False
    kor+=1

# ugyanez for ciklussal, itt látjuk hogy minden esetben végigfut az egész tömbön, hiába van már első körben találatunk - nem erőforrásbarát megoldás
keresett2 = 5
for i in range(0, len(lista1)):
    print(f"for, keresem {i}. kör.")
    if lista1[i]==keresett2:
        print("Van találat: ")

# Hogyan valósítsuk meg ugyanazt az eredmény for ciklussal, mint amit a while-al sikerült megoldani?
# használjuk a break parancsot, ez azonnal megszakítja a for ciklus futását, amint teljesül a feltétel
for i in range(0, len(lista1)):
    print(f"for(break), keresem {i}. kör.")
    if lista1[i]==keresett2:
        print("Van találat: ")
        break

# do while nem létezik pythonban, kerülőmegoldással tudod megoldani...





