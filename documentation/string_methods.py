# String methods / string metódusok
# A python számos beépített funkciót tartalmaz stringekkel való műveletekre

txt = "Hello World"
long_txt = "Lorem ipsum asd dolor sit amet, consectetur adipiscing elit. Sed asd do eiusmod tempor asd incididunt ut labore et dolore magna aliqua."
num_input = "2021"
num2_input = "2,5"
multi = '''
asd
asfdfgdf
ghkghk
kélké
'''

# szoveg.upper() - Mindent nagybetűre cserél
print(f"txt.upper(): {txt.upper()}")

# szoveg.lower() - Mindent kisbetűre cserél
print(f"txt.lower(): {txt.lower()}")

# szoveg.capitalize() - Nagy kezdőbetűt kap a string (nem minden szó, csak az első)
print(f"txt.capitalize(): {txt.capitalize()}")

# szoveg.title() - Nagy kezdőbetűt kap minden szó a stringen belül
print(f"txt.title(): {txt.title()}")

# szoveg.count("keresnivaló") - Rákeres és megszámolja, hogy a keresett szó/szórészlet hányszor szerepel a stringben
print(f"txt.count('el'): {txt.count('el')}")

# szoveg.endswith("keresnivaló") - logikai értékkel(True/False) tér vissza, azt vizsgálja hogy milyen szövegrészletre végződik a string
print(f"txt.endswith('ld'): {txt.endswith('ld')}")

# szoveg.find("keresnivaló") - visszadja azt az indexet, ahol az első találat található
print(f"long_txt.find('do'): {long_txt.find('do')}")

# szoveg.isalnum() - Alphanumeric Ellenőrzi, hogy a string csak betűkből és számokból áll-e(ilyenkor true). Szóköz, spec karaktereknél false értéket ad.
print(f"txt.isalnum(): {txt.isalnum()}")

# szoveg.isalpha() - Ellenőrzi, hogy csak betűket tartalmaz-e(ez esetben true). Szóköz, írásjel, számok esetén false lesz.
print(f"txt.isalpha(): {txt.isalpha()}")

# szoveg.isdigit() - Ellenőrzi, hogy csak számokat tartalmaz-e (ez esetben true)
print(f"num2_input.isdigit(): {num2_input.isdigit()}")

# szoveg.isnumeric() - Ellenőrzi, hogy csak számokat tartalmaz-e (ez esetben true)
print(f"num2_input.isnumeric(): {num2_input.isnumeric()}")

# szoveg.isspace() - Ellenőrzi, hogy csak szóközt tartalmaz-e a string.
print(f"txt.isspace(): {txt.isspace()}")

# szoveg.istitle() - Ellenőrzi, hogy cím formátumban van-e a szöveg (minden szó nagy kezdőbetű)
print(f"txt.istitle(): {txt.istitle()}")

#szoveg.isupper() - Ellenőrzi, hogy a csak nagybetűket tartalmaz-e a szöveg(csak ebben az esetben true)
print(f"txt.isupper(): {txt.isupper()}")

# szoveg.islower() - Az előbbi ellenkezője
print(f"txt.islower(): {txt.islower()}")

# szoveg.join([listaelemek]) - Iterációval összeszerkeszti a szövegünket a lista elemekkel
print(f"txt.join(['hr','st']): {txt.join(['hr','st'])}")

# szoveg.replace(eredeti_szoveg, uj_szoveg) - lecserélheted a szövegrészletet valami másra
print(f"long_txt.replace('asd','***'): {long_txt.replace('asd','***')}")

# szoveg.split('character') - Listára bontja a stringet a megadott karakter alapján. Ha szavakra akarsz bontani egy szöveget, előtte az írásjeleknél replace-el érdemes a spec karaktereket lecserélni a semmire
print(f"long_txt.split(' '): {long_txt.split(' ')}")

# szoveg.splitlines() - sortörésenként bontja listára a string elemeit, nagyon jó szöveg beolvasásnál, ha soronként szeretnénk listába tölteni
print(f"multi.splitlines(): {multi.splitlines()}")

# szoveg.startswith('character') - Ellenőrzi, hogy adott karakterrel kezdődik-e a lista
print(f"txt.startswith('H'): {txt.startswith('H')}")


