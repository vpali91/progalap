#Készíts el 4 funkciót, amik 2 számot várnak paraméterként
#Kérj be 2 számot és a 4 matematikai operátor egyikét:
    #+,-,*,/
#Írj egy olyan funkciót, ami 3 paramétert vár, 2 szám és
    # egy operátor
# Ez a funkció dönste el, hogy melyik számításos 
    #funkciót kell meghívni a 4-ből, az alapján melyik 
    #operátor lett megadva
# Ha rossz operátort ad meg a felhasználó, írja ki.
# írd ki a számítások eredményét

def osszead(n1,n2):
    return n1+n2

def kivon(n1,n2):
    return n1-n2

def osztas(n1,n2):
    return n1/n2

def szorzas(n1,n2):
    return n1*n2

def calculator(n1,n2,operator):
    result =0
    if operator == '+':
        result = osszead(n1,n2)
    elif operator == '-':
        result = kivon(n1,n2)
    elif operator == '/':
        result = osztas(n1,n2)
    elif operator == '*':
        result = szorzas(n1,n2)
    print(f"{n1}{operator}{n2}={result}")

szam1 = int(input("Szám1: "))
szam2 = int(input("Szám2: "))
operator = input("Operátor +-/* :")
if operator == '+' or operator == '-' or operator == '*' or operator == '/':
    calculator(szam1,szam2,operator)
else:
    print("Rossz operátor")
