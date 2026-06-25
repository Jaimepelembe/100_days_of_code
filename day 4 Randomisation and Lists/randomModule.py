#Ao criar um arquivo com o mesmo nome de um modulo em python, ele vai importar o arquivo que eu criei ao inves do modulo.

import random
import myModule

#Generating intagers
numero = random.randint(1,10)
print(numero) 

#Calling a module
#print(f"My favorite number is {myModule.favoriteNumber}")

#Generating Random values between 0 and 1
randomNumber=random.random()

#Generating floats
randomFloat=random.uniform(1,10)
print(randomFloat)
#floatNumber=randomNumber*10
#print(floatNumber)

def headsOrTails():
    #Heads=0 and Tails=1
    number=random.randint(0,1)
    if number == 0:
        print("Heads")
    else:
        print("Tails")

for i in range(4):
    headsOrTails()
