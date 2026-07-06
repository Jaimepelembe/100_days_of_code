#Introduction
def evenOrOdd(number):
    """"Return if a number is even or odd"""

    if number%2==0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


evenOrOdd(27)
evenOrOdd(2026)

#With default parameters
def greet(name="Samora"):
    """Greets a person using it's name. Default name is Samora"""
    print(f"Hello {name}")

greet()
greet("Mawhoo")

#Variable length parameters
## Positional arguments
def printNumbers(n1,n2,n3): # Accept a specific number of parameters
    pass

def printNumbers2(*numbers): # Accept multiple parameters
    print(numbers)
    print("--------------------")
    for number in numbers:
        print(number)
    
printNumbers2(2,4,6,8,10,12)


#Keywords arguments : All the parameters will be in the form of key-value pairs

def printPerson(**kwargs):
    print(kwargs)
    for name, age in kwargs.items():
        print(f"{name}:{age}")

printPerson(name="Jaime",age=21) 
