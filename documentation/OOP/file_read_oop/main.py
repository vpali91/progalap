# importálni kell az osztályunkat tartalmazó fájlt és az osztályunk, melyeknek most azonos neve van
from NPC import NPC

# üres npc lista, amely npc objektumainkat fogja tartalmazni
npc_list = []
# fájl beolvasás relatív útvonallal, ilyenkor a fájl-nak ugyanabban a mappában kell lennie
f=open("npcs.txt")
txt = f.read()
# npc_lines listába bekerül soronként a beolvasott szöveg
npc_lines = txt.splitlines()

# for ciklussal végigmegyünk a sorokat tartalmazó listán
for i in range(len(npc_lines)):
    # split paranccsal körönként minden egyes sort felosztunk a ',' karakterek alapján olyan listába, amely az egy sorba tartozó tulajdonságokat ossza fel külön elemekre
    # ez minden ciklusban felülíródik az új sor elemeivel
    npcline_character = npc_lines[i].split(',')
    # npc_generator nevű objektum példányosítása az adott sorba tartozó értékekkel, minden körben felülíródik az új értékekkel
    npc_generator = NPC(npcline_character[0], npcline_character[1], int(npcline_character[2]), npcline_character[3])
    # npc_list listához hozzáadjuk az npc_generator objektumot, minden körben új objektummal bővül
    npc_list.append(npc_generator)

# Az objektumokat tartalmazó lista kiíratása
for npc in npc_list:
    print(f"{npc.name}, {npc.race}, {npc.hp}, {npc.immortal}")

# Keresd meg az összes halhatatlan karaktert(ahol immortal == True)
immortal_list =[]
for npc in npc_list:
    # ha igaz a feltétel, akkor az adott objektumot hozzáadja immortal_list-hez, ha nem akkor nem történik semmi
    if npc.immortal == True:
        immortal_list.append(npc)

# immortal lista kiíratása
print("Immortals: ")
for npc in immortal_list:
    print(f"{npc.name}, {npc.race}, {npc.hp}, {npc.immortal}")

# Maximumkeresés, keresd meg a legtöbb hp-vel rendelkező npc karaktert
# max érték beállítása, itt mindig valami irreálisan alacsony értéket kell megadni. Ez mindig felülíródik a nagyobb hp-jű objektum hp értékével
max = 0
# egy npc objektum, amit mindig felülírunk, ha nagyobb hp-bel rendelkező objektumot találunk
max_hp_npc = npc_list[0]
for npc in npc_list:
    # abban az esetben, ha az éppen vizsgált objektum hp-je nagyobb max-nál, akkor felülírjuk max és max_hp_npc értékét
    # az első körben mindenképpen felülíródik max értéke, utána nem feltétlenül, csak ha nagyobbat találunk
    if npc.hp > max:
        max = npc.hp
        max_hp_npc =npc

print(f"Max hp npc: {max_hp_npc.name}, hp: {max_hp_npc.hp}")

# Minimumkeresés, keresd meg a legtöbb hp-vel rendelkező npc karaktert
# min érték beállítása, itt mindig valami irreálisan magas értéket kell megadni. Ez mindig felülíródik a kisebb hp-jű objektum hp értékével
min = 10000
# egy npc objektum, amit mindig felülírunk, ha kisebb hp-bel rendelkező objektumot találunk
min_hp_npc = npc_list[0]
for npc in npc_list:
    # abban az esetben, ha az éppen vizsgált objektum hp-je kisebb min-nél, akkor felülírjuk min és min_hp_npc értékét
    # az első körben mindenképpen felülíródik min értéke, utána nem feltétlenül, csak ha nagyobbat találunk
    if npc.hp < min:
        min = npc.hp
        min_hp_npc =npc

print(f"Min hp npc: {min_hp_npc.name}, hp: {min_hp_npc.hp}")

# Megszámolás, nord karakterek megszámolása
# counter számláló beállítása 0-ra, ezt növeljük egyesével minden találatnál
counter = 0
# for ciklussal végigmegyünk minden npc objektumon
for npc in npc_list:
    # ha megegyezik a race a nord szóval, akkor 1-el növeljük counter értékét
    if npc.race == "nord":
        counter +=1

print(f"Nords: {counter}")
