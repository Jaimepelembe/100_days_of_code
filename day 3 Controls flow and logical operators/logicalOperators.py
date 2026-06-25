print("Welcome to the rollercoaster!")
height=float(input("What is yor height? "))
age=int(input("What is your age? "))
ticketPrice=0

if height >= 120:
    print("You can Ride")
    if age > 18:
        print("Adult tickets are $12")
        ticketPrice=12
    elif age>=12 and age <=18:
        print("Youth tickets are $7")
        ticketPrice=7
    else:
        print("Child tickets are $5")
        ticketPrice=5

    wantsPhoto = input("Do you want a photo take? Type y for Yes and n for No. ") 
    if wantsPhoto == "y":
        ticketPrice+=3
     
    print(f"Please pay ${ticketPrice}")

else:
    print("You can not Ride")