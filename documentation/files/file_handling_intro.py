# Python file használat

# File létrehozása nev = open("path/file_nev.txt, "mód"), ez esetben a mód=a, ami append, tehát létrehozza a file-t ha nem létezik
# továbbá append esetén a korábbi tartalom megmarad, ahhoz fűzi hozzá az új szöveget
f = open("d://demofile.txt", "a")
# Itt adódik hozzá az új szöveg
f.write("Új tartalom, asdfasf fasfa")
# zárni is kell, miután open is volt
f.close()

# File létrehozása nev = open("file_nev.txt, "mód"), ez esetben a mód=w, ami write, tehát létrehozza a file-t ha nem létezik
# továbbá erite esetén a korábbi tartalom törlődik, azt írja felül az új tartalom
f = open("d://demofile.txt", "w")
# Itt adódik hozzá az új szöveg
f.write("Újabb tartalom, asdfasf fasfa")
# zárni is kell, miután open is volt
f.close()

# File olvasása nev = open("path/file_nev.txt", "r"), ez esetben r = read, tehát olvasni
f = open("D:\\demofile.txt", "r")
print(f.read())
