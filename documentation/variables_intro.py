# változók típusai
a = 1 # int, egész szám
b = 1.5 # float, tört szám
c = True # bool, azaz logikai változó
d = "asd" # str, azaz string

camelCase = "camel"
PascalCase = "Pascal" # bár működik, csak osztályok elnevezésénél illik használni
snake_case = "snake"
#kebab-case = "kebab" ez nem működik pythonban
print(camelCase + PascalCase + snake_case)
# a változó nem kezdődhet számmal, de rakhatsz számot bele: pl: a1
# a változó nem tartalmazhat szóközt, speciális karaktert, ékezetes se legyen
# a tiszta kód jegyében próbálj mindig beszédes nevet adni nekik, lehetőleg angol nevekkel, hogy bárki ránéz, tudja miről van szó

# azonons típusú változók kiíratásakor + jellel válasszuk el a kiírandó változókat
print(a + b)
print("asd" + " " + "valami")

# Ha eltérő típusú változót akarsz kiíratni, akkor , jellel válasszuk el a változókat. pl string és szám, stb...
print (a , d)
print("asd" , a)
#f string kiíratás során f betűt rakunk az idézőjel elé, így a {} jel közé rakott változó értékét fogjuk kiíratni
print(f"asd {a}")

# input bekérésnél az input parancsot használjuk, a zárójelen belül idézőjelek közé írjuk, amit szeretnénk közölni a felhasználóval
bekert_szam = input("aDj meg egy számot!")
print("A bekért szám: " + bekert_szam) # Fontos! Az inputként bekért értékek mindig stringek
#cast-olás, amikor az adott változónak megváltoztatjuk a típusát. Pl stringet számmá, vagy tört számot egésszé, vagy fordítva
igazi_szam = int(bekert_szam)
print(a + igazi_szam) # így már össze tudod adni számmal, hiszen már szám

f = input("adj meg egy szöveget!")
# a len() egy beépített parancs, zárójelben egy idézőjelek közé tett szöveget, vagy string típusú változót teszünk és megszámolja a karaktereit whitespace-el együtt
hossz = len(f)
print(f"A szöveg hossza {hossz}")
