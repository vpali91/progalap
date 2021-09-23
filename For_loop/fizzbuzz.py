# Ha Írasd ki a számokat 1-100-ig.
# Ha 3-al osztható akkor a számhelyett "Fizz"-t,
# ha 5-el "Buzz"-t,
# ha mindkettő, akkor "FizzBuzz"-t írjon ki a szám helyett

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz!")
    elif n % 3 == 0:
        print("Fizz!")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)