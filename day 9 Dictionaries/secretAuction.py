from validationFunctions import validateString, validateFloat
auctionDictionary={} #Key is the user name and value is the bid value.
endProgram=False

logo="""

  ____________
             /
    )________(
    |""""""""|_.-._,.-----------.,_.-._
    |        |  |  |               |  | ''-.
    |        |__|  |_             _|  |_..-'
    |________|  '-'''-----------''   '_'
    )""""""""(
   /___________\\
  .-------------.
 /_______________\\

"""

print(logo)

while not endProgram:
    userName=validateString("What is your name?: ")
    userBid= validateFloat("What is your bid?: $ ")
    userchoose=validateString("Are there any other bidders? Type 'yes' or 'no'\n ")
    auctionDictionary[userName]=userBid
    if userchoose == "no":
        maxBid=0
        userWin=""
        for name, bid in auctionDictionary.items():
            if bid> maxBid:
                maxBid=bid
                userWin=name
        endProgram=True

        print(f"The winner is {userWin} with a bid of ${maxBid}")