MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 120,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 140,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    #True, ha a rendelés megoldható, False ha az összetevők elfogytak.
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Bocs nincs elég {item}.")
            return False
    return True


def process_coins():
    #Feldolgozza a bedobott érméket
    print("Dobjon be érméket")
    total = int(input("Hány 100-as: ")) * 100
    total += int(input("Hány 50-es: ")) * 50
    total += int(input("Hány 20-as: ")) * 20
    total += int(input("Hány 10-es: ")) * 10
    return total


def is_transaction_successful(money_received, drink_cost):
    #True, ha a fizetés elfogadva, False ha kevés a pénz
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Itt a viszajáró {change}Ft apróban.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Bocs kevés a pénz. Pénz visszaadva.")
        return False


def make_coffee(drink_name, order_ingredients):
    # Levonja az felhasznált összetevőket
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Itt az italod: {drink_name} ☕️ ")


is_on = True

while is_on:
    choice = input("​Mit szeretnél? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
