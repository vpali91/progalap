# Math methods
import math
list = [1, 5, 7, 9, 3]

# faktoriális: math.factorial(5) -- ugyanez teljesen kiírva: 5*4*3*2*1
print(math.factorial(5))

#math.fabs(szam) - Abszolút érték, negatív számot pozitívra váltja, a pozitív az pozitív marad
print(math.fabs(-1))

# math.floor(szam) - Nem kerekít! Levágja a tizedes jelet
print(math.floor(5.6))

# math.fsum(lista) - Összeadja a lista számait
print(math.fsum(list))

# math.pow(szám, hatványérték) - hatványozás, a példában 3 a negyediken van.
print(math.pow(3, 4))

# math.sqrt(szám) négyzetgyök
print(math.sqrt(9))

# PI
print(math.pi)

#round(szam, mennyi_tizedesjel_marad)
print(round(math.pi, 2))
