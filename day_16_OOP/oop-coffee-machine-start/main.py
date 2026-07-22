from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu= Menu()
coffeeMk=CoffeeMaker()
moneyMc=MoneyMachine()
isOn=True

while isOn:
    userChoose= input(f"What would you like? ({myMenu.get_items()}): ")

    if userChoose=="off":
        isOn=False
    elif userChoose == "report":
        coffeeMk.report()
        moneyMc.report()

    else:
        drink=myMenu.find_drink(userChoose)
 
        if coffeeMk.is_resource_sufficient(drink):
            if moneyMc.make_payment(drink.cost):
                coffeeMk.make_coffee(drink)

  