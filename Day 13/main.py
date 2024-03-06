from menu import MENU, resources

money = 0

coffee_cost_dictionary = {}

for coffee in MENU:
    coffee_cost_dictionary[coffee] = MENU[coffee]["cost"]


def calculate_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total


def coffee_price(coffee_name):
    return MENU[coffee_name]["cost"]


def enough_resources(coffee_name):
    if MENU[coffee_name]["ingredients"]["water"] > resources["water"]:
        print("Not enough water.")
        return False
    elif coffee_name != 'espresso' and (MENU[coffee_name]["ingredients"]["milk"] > resources["milk"]):
        print("Not enough milk.")
        return False
    elif MENU[coffee_name]["ingredients"]["coffee"] > resources["coffee"]:
        print("Not enough coffee.")
        return False
    return True


def update_resources(coffee_name):
    resources["water"] -= MENU[coffee_name]['ingredients']["water"]
    if coffee_name != 'espresso':
        resources["milk"] -= MENU[coffee_name]['ingredients']["milk"]
    resources["coffee"] -= MENU[coffee_name]['ingredients']["coffee"]


machine_on = True


while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        machine_on = False
        break

    for keys in coffee_cost_dictionary:
        print(f"{keys}: $ {coffee_cost_dictionary[keys]}")

    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money}")
    else:
        if enough_resources(user_input):
            user_money = calculate_money()
            if user_money >= coffee_price(user_input):
                change = round(user_money - coffee_price(user_input),2)
                print(f"Here is your ${change} in change.")
                print(f"Enjoy your {user_input}☕\n")
                money += coffee_price(user_input)
                update_resources(user_input)
            else:
                print("Not enough coins 😒\n")






