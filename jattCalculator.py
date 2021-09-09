# Készíts jatt kalkulátort
# 1. Üdvözöljön a program
# 2. Kérje be mennyi a számla
# 3. Kérje be, hány százalék jattot akarsz adni
# 4. kérje be, hány ember osztozik a társaságban a jattfizetésen
# 5. Írja ki,mennyit kell fizetnie 1 embernek

print("Welcome to tip calculator")
bill = float(input("Total bill:"))
percentage = float(input("What percentage tip will you give:"))
people = int(input("How many people to split the bill"))
result = (bill + bill*percentage/100)/people
print(f"Each person should pay: {result}")
