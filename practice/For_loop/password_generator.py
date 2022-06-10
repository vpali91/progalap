#Password Generator Project
import random
# Ezek a listák tartalmazzák azokat a karaktereket, amelyekből ki lesz generálva a jelszó
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?")) #a betű karakterek számát adod meg
nr_symbols = int(input(f"How many symbols would you like?")) # szimbólumok számát adod meg
nr_numbers = int(input(f"How many numbers would you like?")) # A számok számát adod meg

#Könnyű szint - A karakterek elrendezése nincs össszekeverve:
#Pl: 4 betű, 2 szimbólum, 2 szám = JduE&!91

# Egy üres string, amihez majd hozzáadogatjuk a randomizált karaktereket
password = ""
 #random.choice(listanév) Ez a listából véletlenszerűen kiválaszt egy elemet. Ez ki lehetne váltani azzal, ha generálsz egy random számot és utána lista[randomszám]-ot kérsz le
 #a for ciklus annyiszor fut le, ahány db-ot kért a felhasználó az adott típusú karakterből
for char in range(0, nr_letters):
   password += random.choice(letters)

for char in range(0, nr_symbols):
   password += random.choice(symbols)

for char in range(0, nr_numbers):
   password += random.choice(numbers)

print(password)

#Nehéz szint, itt keverten jelennek meg a karakterek:
#pl: 4 betű, 2 szimbólum, 2 szám = g^2jk8&P

#üres lista, amit azért hozunk létre, mert ehhez adjuk hozzá a jelszó karaktereit, azért hogy össze tudjuk keverni a sorrendjüket
password_list = []

for char in range(0, nr_letters):
  password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
  password_list += random.choice(symbols)

for char in range(0, nr_numbers):
  password_list += random.choice(numbers)

print(password_list)
#random.shuffle(listanév) ez összekeveri a lista elemeinek a sorrendjét
random.shuffle(password_list)
print(password_list)

# itt adjuk hozzá password stringhez a kevert lista elemeit
password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")