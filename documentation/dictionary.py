# Dictionary
# dictionary segítségével adatokat tárolhatunk kulcs: érték párosításban, hasonlóképp mint ahogy egy szótár is felépül
# a dictionary egy olyan collection, ami rendezve van, módosítható és nem enged duplikációt

# így épül fel: név = {"kulcs1" : "érték1", "kulcs2" : "érték2"}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Így a listához hasonlóan ki tudjuk íratni a teljes dictionary-t, igaz így nem tudunk dolgozni vele
print(thisdict)

# Úgy tudjuk megadni egy meghatározott kulcshoz tartozó értékét, ha hivatkozunk a kulcsra: dictionary["kulcs1"]
print(thisdict["brand"])

# Felül is írhatjuk a kulcshoz tartozó értéket:
thisdict["year"] = 1965

# Így kérhetünk le egy listát a dictionary kulcsairól:
key_list = thisdict.keys()
print(key_list)

# ezt követően hozzáférhetünk az értékekhez
for item in key_list:
    print(thisdict[item])

# Akár így is lekérhetjük az értékeket:
values_list = thisdict.values()
print(values_list)

# Kulcs ellenőrzése hogy létezik-e, ez azért jó, mert nem crashel, ha rossz kulcscsal próbálkozunk
if "model" in thisdict:
    print(f"Igen létezik 'model' kulcs, értéke: {thisdict['model']}")

# Elem hozzáadása nev["uj_kulcs"] = "uj ertek"
thisdict["color"] = "blue"

# ez is működik
thisdict.update({"second_color": "white"})
print(thisdict)

# elem eltávolítása nev.pop("kulcs")
thisdict.pop("second_color")
print(thisdict)

# Kiíratás módok iterációval
for item in thisdict.values():
    print(item)

for item in thisdict.keys():
    print(item)

# Nested dictionaries - Egymásba ágyazott dictionary: dictionary a dictionary-ben
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#kiíratás és hozzáférés
print(myfamily["child1"]["name"])
