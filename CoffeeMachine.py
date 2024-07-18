MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
coin_values = {
    'penny': 1,
    'nickel': 5,
    'dime': 10,
    'quarter': 25
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

end_coffee = False
current_water = resources["water"]
current_milk = resources["milk"]
current_coffee = resources["coffee"]
money = 0


def turnoff(turn):
    if turn == "off":
        global end_coffee
        end_coffee = True


#resources function to check if they are enough
def resources(input):
    global end_coffee
    global current_coffee, current_milk, current_water
    """checks if resources are enough"""
    espresso_ingredients = MENU["espresso"]["ingredients"]
    latte_ingredients = MENU["latte"]["ingredients"]
    cappuccino_ingredients = MENU["cappuccino"]["ingredients"]
    if input == "espresso":
        if (current_water < espresso_ingredients["water"]):
            print("Sorry there is not enough water.")
            return False
        elif (current_coffee < espresso_ingredients["coffee"]):
            print("Sorry there is not enough coffee.")
            return False
    elif input == "latte":
        if (current_water < latte_ingredients["water"]):
            print("Sorry there is not enough water.")
            return False
        elif current_milk < latte_ingredients["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif current_coffee < latte_ingredients["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    elif input == "cappuccino":
        if current_water < cappuccino_ingredients["water"]:
            print("Sorry there is not enough water.")
            return False
        elif current_milk < cappuccino_ingredients["milk"]:
            print("Sorry there is not enough milk.")
            return False

    return True


def report(name):
    """Function that displays report"""
    global money, current_water, current_milk, current_coffee
    if name == "report":
        print(f"Water: {current_water}ml\nMilk: {current_milk}ml\nCoffee: {current_coffee}ml\nMoney: ${money}")


def coins(coin):
    """transaction"""
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    if coin == "espresso" or coin == "latte" or coin == "cappuccino":
        print("Please insert coins. ")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)
    total_dollars = total_cents / 100
    return total_dollars


def transaction(trans, dollars):
    global money, current_water, current_milk, current_coffee
    espresso_ingredients = MENU["espresso"]["ingredients"]
    latte_ingredients = MENU["latte"]["ingredients"]
    cappuccino_ingredients = MENU["cappuccino"]["ingredients"]
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    if trans == "espresso":
        if dollars < espresso_cost:
            print("Sorry there is not enough money. Money refunded")
        elif (dollars == espresso_cost):
            money += dollars
            current_water -= espresso_ingredients["water"]
            current_coffee -= espresso_ingredients["coffee"]
        else:
            money += espresso_cost
            current_water -= espresso_ingredients["water"]
            current_coffee -= espresso_ingredients["coffee"]
            difference = round(dollars - espresso_cost, 2)
            print(f"Here is ${difference} dollars in change.")
    elif trans == "latte":
        if dollars < latte_cost:
            print("Sorry there is not enough money. Money refunded")
        elif (dollars == latte_cost):
            current_milk -= latte_ingredients["milk"]
            current_coffee -= latte_ingredients["coffee"]
            current_water -= latte_ingredients["water"]
            money += dollars
        else:
            money += latte_cost
            current_milk -= latte_ingredients["milk"]
            current_coffee -= latte_ingredients["coffee"]
            current_water -= latte_ingredients["water"]
            difference = round(dollars - latte_cost, 2)
            print(f"Here is ${difference} dollars in change.")
    elif trans == "cappuccino":
        if dollars < cappuccino_cost:
            print("Sorry there is not enough money. Money refunded")
        elif (dollars == cappuccino_cost):
            money += dollars
            current_milk -= cappuccino_ingredients["milk"]
            current_coffee -= cappuccino_ingredients["coffee"]
            current_water -= cappuccino_ingredients["water"]
        else:
            money += cappuccino_cost
            current_milk -= cappuccino_ingredients["milk"]
            current_coffee -= cappuccino_ingredients["coffee"]
            current_water -= cappuccino_ingredients["water"]
            difference = round(dollars - cappuccino_cost, 2)
            print(f"Here is ${difference} dollars in change.")


while not end_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    turnoff(choice)
    report(choice)
    if resources(choice):
        total_dollars = coins(choice)
        transaction(choice, total_dollars)
