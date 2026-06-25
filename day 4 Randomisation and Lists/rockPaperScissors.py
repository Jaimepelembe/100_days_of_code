import random
from packages.validationFunctions import inputValidation


rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

print("Welcome to Rock Papper Scissor game!")
playerChoose=inputValidation("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor",(0,1,2))

