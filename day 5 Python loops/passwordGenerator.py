from validationFunctions import validateInteger
from random import randint

listLetters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
listNumbers=['0','1','2','3','4','5','6','7','8','9']
listSymbols=['!','#','$','%','&','(',')','*','+','^','?','{','}']


print("Welcome to the PyPassword Generator")
nrLetters=validateInteger("How many letters would you like in your password? \n")
nrSymbols=validateInteger("How many symbols would you like? \n")
nrNumbers=validateInteger("How many numbers would you like? \n")



def lettersPassword(nrLetters):
    passwordLetters=""
    for i in range(nrLetters):
        choice=randint(0,25)
        letterCase=randint(0,1) # 0:Uppercase and 1:Lowercase

        if letterCase == 0:
            passwordLetters+=listLetters[choice].upper()
        else:
            passwordLetters+=listLetters[choice]

    return passwordLetters



def numberOrSymbolsPassword(lenght,listElements):
    password=""
    for i in range(lenght):
        choice=randint(0,len(listElements)-1)
        password+= listElements[choice]
    
    return password



passwordLetters=lettersPassword(nrLetters)
passwordSymbols = numberOrSymbolsPassword(nrSymbols,listSymbols)
passwordNumbers= numberOrSymbolsPassword(nrNumbers,listNumbers) 



#Easy version:
# Sequence of the password: Letters, symbols and numbers
def easyPassword():
    return passwordLetters + passwordSymbols + passwordNumbers



#Hard version:
# The final password does not follow a pattern: Ex: x$d24g*f9
def hardPassword(passwordLetters,passwordSymbols,passwordNumbers):
    passwordLetters=list(passwordLetters) # Uma String é um iterável por isso pode ser transformada em uma lista.
    passwordSymbols = list(passwordSymbols)
    passwordNumbers = list(passwordNumbers)
    listPasswords=[passwordLetters,passwordSymbols,passwordNumbers]
    password=""
    print(listPasswords)

    while len(listPasswords) >=1:
        choiceOfList= randint(0,len(listPasswords)-1)
        lenghtList=len(listPasswords[choiceOfList])
        if lenghtList >=1:
            indexOfElement = randint(0,lenghtList-1)
            element=listPasswords[choiceOfList].pop(indexOfElement)
            password+=element
            if len(listPasswords[choiceOfList]) < 1:
                listPasswords.pop(choiceOfList)
        else:
            listPasswords.pop(choiceOfList)
    return password


passwordFormat=validateInteger("Type 1 for easy format and 2 for hard format: ")
password=""
if passwordFormat == 1:
    password = easyPassword()
else:
    password = hardPassword(passwordLetters,passwordSymbols,passwordNumbers)

print(f"Your password is: {password}")

