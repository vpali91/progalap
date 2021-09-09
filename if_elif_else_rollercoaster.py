print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

#elif csak abban az esetben fog lefutni ha az if feltétel nem teljesült és elif feltétele igaz
# próbáld ki! Ha az elifet lecseréled if-re és olyan feltételt adsz meg, ami az előző if feltételre is igaz, akkor mindkét if alatti parancs le fog futni sorban
if height > 120:
    print("You can get to the rollercoaster!")
    age = int(input("What is yout age?"))
    if age < 12:
        bill = 5
        print(f"Ticket: {bill}$!")
    elif age <= 18:
        bill = 7
        print(f"Ticket:  {bill}$!")
    else:
        bill = 12
        print(f"Ticket: {bill}$!")
else:
    print("Go home!")
