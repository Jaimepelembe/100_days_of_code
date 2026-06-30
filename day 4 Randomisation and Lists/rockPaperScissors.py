import random
from validationFunctions import validateInteger


rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

gameImages=[rock,paper,scissors]


"""Rulers:
#Rock wins agains scissors;
#Scissors win against paper;
#Paper wins against rock;
"""



print("Welcome to Rock Papper Scissor game!")
playerChoose=validateInteger("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
computerChoose=random.randint(0,2)

if playerChoose>=0 and playerChoose<=2:
    print(gameImages[playerChoose]) # Prints the player choose
    print("Computer chose:")
    print(gameImages[computerChoose]) # Prints the computer choose

    if playerChoose == computerChoose:
        print("It's a draw")
    
    elif playerChoose == 0 and computerChoose == 2:
        print("You win")
    
    elif playerChoose == 2 and computerChoose == 1:
        print("You win")
    
    elif playerChoose == 1 and computerChoose == 0:
        print("You win")
    
    else:
        print("You lose")

else:
    print("You selected an invalid number, try again.")