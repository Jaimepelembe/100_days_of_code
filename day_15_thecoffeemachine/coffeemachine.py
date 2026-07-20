from validationFunctions import inputValidation,inputInteger
from fileOperations import readFile, writeFile,readJsonFile,writeObjectInJson

drinks={
"espresso": { 
    "ingredients":{"water":50,"coffee":18},
    "cost":1.50
             },

"latte":{
    "ingredients":{"water":200,
                   "coffee":24,
                   "milk":150
                   },
    "cost":2.50
},
"cappuccino":{
    "ingredients":{
        "water":250,
        "coffee":24,
        "milk":100
    },
    "cost":3.0
}
}

machineResources={
    "water":300, #ml
    "milk":200, #ml
    "coffee":100 #g
}




def reportResources():
    """"Makes a report of the machine resources."""
    for key,value in machineResources.items():
        key=key.capitalize()
        if key =="Coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: {value}ml")
    
    print(f"Money: ${totalMoney}" )

def verifyQuantityResource(resourceName,minimun):
    """Verify if there are the minimun amount of a certain resource required to make the drink. Returns True when are and False Otherwise"""
    if machineResources[resourceName] >=minimun:
        return True
    else:
        print(f"Sorry there is not enough {resourceName}")
        return False

def insertCoins():
    """Receives the money inserted by the user on the machine and return the total value."""

    print("Please insert the coins: ")
    quarters= inputInteger("How many quarters?: ")
    dimes= inputInteger("How many dimes?: ")
    nickles= inputInteger("How many nickles?: ")
    pennies= inputInteger("How many pennies?: ")

    return 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies 

def checkTransaction(drinkCost,userMoney):
    """Check if the user inserted enough money in the machine to buy the drink. Returns True or False"""

    if userMoney < drinkCost:
        print(f"Sorry ${userMoney} is not enough money, the drink cost ${drinkCost} dollars. Money refunded.")
        return False
    elif userMoney== drinkCost:
        return True
    else:
        change= userMoney-drinkCost
        print(f"Here is ${change:.2f} dollars in change.")
        return True

def makeCoffee(drink):
    """Make the drink using the necessary resources. Returns a dictionary of resources updated."""

    drinkIngredients=drinks[drink]["ingredients"]
    amountWater=drinkIngredients["water"]
    amountCoffee=drinkIngredients["coffee"]
    
    #Deduct the resources used to make the drink
    machineResources["water"]= machineResources["water"]-amountWater
    machineResources["coffee"]= machineResources["coffee"]-amountCoffee
    
    if drink != "espresso":
        amountMilk=drinkIngredients["milk"]
        machineResources["milk"]= machineResources["milk"]-amountMilk

    return machineResources

"""
def checkResources(drink):
   # Check if there are enough resources to make a drink. Returns True when are and False otherwise

    drinkIngredients=drinks[drink]["ingredients"]
    amountWater=drinkIngredients["water"]
    amountCoffee=drinkIngredients["coffee"]
    if drink == "espresso":
        if verifyQuantityResource("water",amountWater) and verifyQuantityResource("coffee",amountCoffee):              
            return True
        else:
            return False 
                
    else: # drink =="latte" or drink == "cappuccino"
        amountMilk=drinkIngredients["milk"]
        if verifyQuantityResource("water",amountWater) and verifyQuantityResource("coffee",amountCoffee) and verifyQuantityResource("milk",amountMilk):
                  return True
        else:
            return False 
"""
            
def checkResources2(orderIngredients):
    """Check if there are enough resources to make a drink. Returns True when are and otherwise False"""

    for ingredient in orderIngredients:
        if orderIngredients[ingredient] > machineResources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def addResource(resourceName,difference):
    """Adds a certain amount of resource to the coffee machine. Return a dictionary with the resource updated"""
    if difference>0:
        machineResources[resourceName]=machineResources[resourceName]+difference
        if resourceName !="coffee":
            print(f"You added {difference}ml of {resourceName}.")
        else:
            print(f"You added {difference}g of {resourceName}.")

    return machineResources


def updateResources(machineResources):
    """Update all the resources of the machine. Return a dictionary with all resources updated"""
    actualWater= machineResources["water"]
    actualMilk = machineResources["milk"]
    actualCoffee =machineResources["coffee"]

    differenceWater= maxWater - actualWater
    differenceMilk= maxMilk - actualMilk
    differenceCoffee= maxCoffee - actualCoffee

    machineResources=addResource("water",differenceWater)
    machineResources=addResource("milk",differenceMilk)
    machineResources=addResource("coffee",differenceCoffee)
    
    return machineResources 

#Start the variables
isOn=True
fileName="moneyEarned.txt"
totalMoney=float(readFile(fileName))
#machineResources=readJsonFile(fileResources)

maxWater=machineResources["water"] # 300ml
maxMilk=machineResources["milk"] # 200ml
maxCoffee=machineResources["coffee"]# 100g

while isOn:
    userChoose=inputValidation("What would you like? (espresso/latte/cappuccino): ",["espresso","latte","cappuccino","off","report"])
    if userChoose == "off":
        isOn=False # Ends the program
    elif userChoose =="report":
        reportResources()
       
       # Update a resource if the user want.
        if machineResources["water"] < maxWater or machineResources["milk"] < maxMilk or machineResources["coffee"] < maxCoffee:
            answer= inputValidation("Do you want to add the resources? Type 'y' or 'n': ",["y","n"])
            if answer == "y":
                machineResources=updateResources(machineResources)

    else:
        # check if the resources are sufficient to make the drink
        drinkIngredients=drinks[userChoose]["ingredients"]
        if checkResources2(drinkIngredients):
            #Process coins: Receives the money from the user
            userMoney=insertCoins()
            drinkCost=drinks[userChoose]["cost"]


        # Check if the transaction is successful
            if checkTransaction(drinkCost,userMoney):
                totalMoney+=drinkCost      
                writeFile(fileName,f"{totalMoney}") # Save the total money earned in the text file.
                machineResources=makeCoffee(userChoose)   
                print(f"Here is your {userChoose} ☕. Enjoy!")

      
        


