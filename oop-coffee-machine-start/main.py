from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()

machine_on = True

while machine_on:
    ask_user = input(f"What would you like? ({menu.get_items()}): ")
    coffee_info = menu.find_drink(ask_user)
    if ask_user == 'off':
        machine_on = False
        break
    elif ask_user == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        if coffeeMaker.is_resource_sufficient(coffee_info):
            if moneyMachine.make_payment(coffee_info.cost):
                coffeeMaker.make_coffee(coffee_info)

