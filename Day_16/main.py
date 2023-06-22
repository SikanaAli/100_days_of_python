from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_counter = MoneyMachine()
coffee_menu = Menu()

is_on = True


def check_choice(choice):
    match choice:
        case "report":
            coffee_machine.report()
            money_counter.report()
            return
        case "latte" | "espresso" | "cappuccino":
            drink_ordered = coffee_menu.find_drink(choice)

            have_resource = coffee_machine.is_resource_sufficient(drink_ordered)
            if have_resource:
                money_enough = money_counter.make_payment(drink_ordered.cost)
                if money_enough:
                    coffee_machine.make_coffee(drink_ordered)
            return
        case _:
            global is_on
            is_on = False
            return


while is_on:
    user_choice = input(f"What would you like? {coffee_menu.get_items()}: ")
    check_choice(user_choice)
