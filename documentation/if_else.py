#Logikai operátorok, amiknek az eredménye mindig true, vagy false. <,>, <=, >=, ==, !=
a = 2
b = 5
c = 2

print(a<b)
print(a>b)
print(a==c)
print(a!=c) #ez azt jelenti nem egyenlő, felkiáltójellel meg tudjuk fordítani a true-t false-ra és fordítva
# Fontos! A szimpla egyenlőségjel nem logikai operátor, hanem azzal adunk értéket például a változóinknak, pl a=1

number = int(input("Which number do you want to check?"))

# A % jel az azt mutatja megy, hogy mennyi a maradék osztás után, pl 3%2=1, mivel 3 kettővel osztva 1 maradékot ad. Ugyanígy 5%2=1
# Mivel minden páros szám osztható 2-vel, így mindig nulla maradéknak kell lennie 2-vel osztásnál, ha van maradék, akkor páratlan
# if feltétel, ami vele van egy sorban az mindig egy olyan feltétel, ami TRUE, vagy False. if-nél mindig TRUE-nak kell lenni, ha azt akarjuk lefusson a hozzátartozó kód
# pythonban if, elif és else-nél a sor végén kettőspont van, azok a parancsok, amik hozzá tartoznak(tehát mi történjen akkor...) azok egy tabulátorral beljebb kezdődnek

if (number%2)==0:
    print("Páros") # ez a kiíratás akkor történik meg, ha az if sorban található feltétel igaz
else: 
    print("Páratlan") # ez a kiíratás akkor történik meg, ha az if feltételünk nem teljesüt, tehát minden egyéb esetben...
