# 1. Describe the problem
def describeBug():
    def myFunction():
        for i in range(1,21): # Code fixed.
            if i==20:
                print("You got it")


    myFunction()

    # Describe the problem - Write your answers as commemts:
        # 1.What is the for loop doing
        # A: Is interating from 1 to 19 and verity if i is equal to 20 to print a message.
        # 2. When is the function meant to print "You got it" ?
        # A: Never, because the variable i will not achieve the value 20
        # 3. What are your assumptions about the value of i?
        # A: i will be between 1 and 19.


#describeBug()


# 2. Reproduce the Bug
def reproduceBug():
    from random import randint
    diceImages=["1","2","3","4","5","6"]
    diceNum=randint(0,5) # randint(1,6) The bugs occurs because the index 6 is out of the diceImages range, because the last index is 5. 
    print(diceImages[diceNum])


#reproduceBug()


# 3. Play computer
# Pretend to be a computer and imagine what you will do in each instructioin of the program.

def playComputer():
    year = int(input("What is your year of birth? "))

    if year >=1980 and year <=1994: # year >1980 and year <1994 . For the values
        print("You're a millennial.")
    elif year > 1994:
        print("You're a Gen Z.")

#playComputer()


# 4. Fix the Errors
# Fix the error before continue to program.

def fixErrors():
    """"
    entry=input("How old are you? ")
    if entry.isdigit(): # Or we can use the try except blocks.
        age=int(entry)
        if age > 18:
            print(f"You can drive at age {age}")
    else:
        print(f"{entry} is not a valid digit.")
"""

#Using try and except
    try:
        age= int(input("How old are you? "))
    except ValueError:
        print("You have typed in an invalid number. Please try again with a numberical number.")
        age= int(input("How old are you? "))
    
    if age >18:
        print(f"You can drive at age {age}")
        

fixErrors()


# 5. Use print()

def usePrint():
    wordPerPage=0
    pages=int(input("Number of pages: "))
    wordPerPage=int(input("Number of words per page: ")) #  wordPerPage == int(input("Number of words per page: "))
    totalWords=pages*wordPerPage
    print(totalWords)

#usePrint()