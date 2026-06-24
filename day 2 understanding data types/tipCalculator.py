print("Welcome to the tip calculator!")
totalBill=float(input("What was the total bill? $"))
tipAmount=float(input("How much tip would you like to give 10%,12%, or 15%? "))
numberPeople=int(input("How many people to split the bill? "))
totalPay=(totalBill+totalBill*(tipAmount/100))/numberPeople
print(f"Each person should pay: ${round(totalPay,2)}")