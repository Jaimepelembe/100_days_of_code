from turtle import Turtle,Screen



def canMoveForward(x):
    if x < 250 :
        return True
    else: 
        return False
    

myTurtle=Turtle()
myTurtle.shape("turtle")
myTurtle.color("#04421C") #  #04421C
while True:
    position=myTurtle.position()
    x,y=position

    if canMoveForward(x):
        myTurtle.forward(10)


"""
    if x < 250 and y <250:
        print(x)
        myTurtle.forward(10)
    else:
        myTurtle.left(90)
        break

myTurtle.forward(x)
"""

#Import the screen object
myScreen=Screen()
print(myScreen.canvheight) # object.attribute 
myScreen.exitonclick()