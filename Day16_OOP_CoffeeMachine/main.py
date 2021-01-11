from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# OOP Coffee machine
# Digital coffee machine start

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

# While machine is on
while is_on:
    # Get the list of all available items and store them in options
    options = menu.get_items()

    # Get the user input after displaying the list of all available items
    choice = input(f"What would you like?: ({options}) - ")

    # if user input is off
    if choice == "off":
        # Stop the loop by changing the flag
        is_on = False
    # If the user input is report then display the status of the machine
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
