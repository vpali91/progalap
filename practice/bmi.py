#BMI index, meg kell adni a magasságod méterben(float) és a súlyod egész szám kg-ban(int), ez alapján a testsúlyt elosztod a magassággal és az így kapott eredményt négyzetre emeled(**).
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight)/float(height)**2
print(bmi)
