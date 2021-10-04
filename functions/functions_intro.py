# functions - Funkciók/metódusok használata
# funkciókat arra tudjuk használni, hogy újra tudjuk használni a megírt kódrészletünket azzal, hogy újra meghívjuk
#Fontos!!! A funkciók csak akkor futnak le, ha legalább 1x meghívtuk őket a nevükön

# function paraméter nélkül
def hello():
    print("Hello")

#meghívás
hello()


#function paraméterrel
name = "Pali"
def helloka(name):
    print(f"Hello {name}")

#meghívás
helloka(name)
helloka("Zoli")

#function több paraméterrel
def hellokak(name1, name2, szam):
    if szam>18:
        print(f"Jó estét {name1} és {name2}")
    else:
        print(f"Jó napot {name1} és {name2}")

#meghívás, fontos hogy ahány paraméter van, annyi értéket meg is kell adnod, különben hibára fut
hellokak("Pali", "Zita", 20)

# A metódusok sokkal összetettebbek is lehetnek, ilyenkor válik hasznossá használatuk
def helloka_v2(name):
    #nagy kezdőbetűsre alakítjuk
    name_capital = name.title()
    print(f"Hello2 + {name_capital}")

# name_capital változó egy lokális változó, csak a funkción belül tudunk rá hivatkozni, funkción kívül nem hivatkozhatunk rá
# print(name_capital) #ez hibára is fut

#azok a változók, amiket a funcktionon kívül hozunk létre, ők a globális változók. Ezeket szinte bárhonnan elérjük
name_capital_global = ""

def helloka_v3(name):
    #ha nem írjuk így be, hogy global, akkor lokális változóként viselkedne továbbra is
    global name_capital_global 
    name_capital_global= name.title()
#meghívás
helloka_v3("Sanya")
#itt láthatjuk, hogy sikeresen megváltoztattuk a változó értékét
print(name_capital_global)

#Eddig minden function végrehajtott egy kiíratást, nem mindig akarunk kiírni valamit, ha azt akarjuk hogy eg értéket adjon vissza, azt is meg tudjuk oldani
def calculator(szam1, szam2, operator):
    sum = 0
    if operator == "+":
        sum = szam1 + szam2
        return sum
    elif operator == "-":
        sum = szam1-szam2
        return sum
    elif operator == "/":
        sum = szam1/szam2
        return sum
    elif operator == "*":
        sum = szam1*szam2
        return sum
    else:
        return 0

szam1 = int(input("Adj meg egy számot!"))
operator = input("Adj meg egy operátort! +,-,/,*")
szam2 = int(input("Adj meg egy számot!"))
eredmeny = calculator(szam1, szam2, operator)
print(f"Calculator: {eredmeny}")

#function a functionban
def calcualtion():
    szam1 = int(input("Adj meg egy számot!"))
    operator = input("Adj meg egy operátort! +,-,/,*")
    szam2 = int(input("Adj meg egy számot!"))
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        eredmeny = calculator(szam1, szam2, operator)
        print(f"Calculation: {eredmeny}")
    else:
        print("Rossz operátor")

calcualtion()
# ez még nem a teljes tananyag a funkciókról, lesz még szó az osztályokon belüli működéséről is, de az már OOP szint

