from calculator import *
from validationFunctions import validateFloat, inputValidation,validateString
endProgram=False
tupleOperation=('+','-','*','/')
userChoose="n"

logo='''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''


while not endProgram:

    if userChoose=="n":
        print(logo)
        firstNumber=validateFloat("What's the first number?: ")
        result=0
    else:
        firstNumber=result

    operation=inputValidation("+\n-\n*\n/\nPick an operation: ",tupleOperation)
    secondNumber=validateFloat("What's the second number?: ")
  
    if operation == "+":
        result=addiction(firstNumber,secondNumber)
    elif operation =="-":
        result=subraction(firstNumber,secondNumber)
    elif operation =="*":
        result=multiplication(firstNumber,secondNumber)
    else:
        result=division(firstNumber,secondNumber)
        
    print(f"{firstNumber} {operation} {secondNumber} = {result}")
    userChoose=inputValidation(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'x' to exit\n",('n','x','y'))
    if userChoose =="x":
        endProgram=True