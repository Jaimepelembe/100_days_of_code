from turtle import Turtle,Screen



def moveForward():
    timmy.forward(20)


def moveBackward():
    timmy.backward(20)


def turnLeft():
    timmy.left(10)


def turnRight():
    timmy.right(10)


def drawCircle():
    timmy.circle(100,10)

    
def clearScreen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def closeWindow():
    screen.bye()


"""
leo=Turtle()
leo.color("green")
leo.left(90)
leo.forward(100)
"""

timmy=Turtle()

screen=Screen()

#Event listener
screen.listen()
screen.onkey(moveForward,"w") 
screen.onkey(moveBackward,"s") 
screen.onkey(turnRight,"d") 
screen.onkey(turnLeft,"a") 
screen.onkey(drawCircle,"Right")
#screen.onkey(drawCircleCounterClockwise,"Left")

screen.onkey(clearScreen,"c")
screen.onkey(closeWindow,"Escape")


screen.mainloop()
