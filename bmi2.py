height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

result = round(weight/height**2, 1)

if result < 18.5:
    print(f"{result} underweight")
elif result < 25:
    print(f"{result} normal weight")
elif result < 30:
    print(f"{result} overweight")
elif result < 35:
    print(f"{result} obese")
else:
    print(f"{result} clinically obese")

