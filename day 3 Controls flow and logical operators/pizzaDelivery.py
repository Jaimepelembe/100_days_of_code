from validationFunctions import inputValidation

print("Welcome to Python Pizza Deliveries!")

pizzaSize=inputValidation("What size pizza do you want? S, M or L: ",("S","M","L"))
pepperoni= inputValidation("Do you want pepperoni on your pizza? y or n: ",("y","n"))
extraCheese=inputValidation("Do you want extra cheese? y or n: ",("y","n"))
bill=0

#todo: work out how much they need to pay based on their size choice.
#todo: work out how much to add to their bill based on their pepperoni choice.
#todo: work out their final amount based on wheter if they want extra cheese.


if pizzaSize == "S":
    bill+=15
    if pepperoni=="y":
           bill+=2
else:           
    if pizzaSize == "M":
        bill+=20
    else:
        bill+=25

    if pepperoni=="y":
           bill+=3

if extraCheese =="y":
     bill+=1
    
print(f"The total bill is ${bill}")