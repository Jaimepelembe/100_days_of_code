from turtle import Turtle,Screen



def moveForward():
    timmy.forward(20)


def moveBackward():
    timmy.backward(20)


def turnLeft():
    timmy.left(90)


def turnRight():
    timmy.right(90)

def closeWindow():
    screen.bye()

timmy=Turtle()




screen=Screen()

#Event listener
screen.listen()
screen.onkey(moveForward,"Up") 
screen.onkey(moveBackward,"Down") 
screen.onkey(turnRight,"Right") 
screen.onkey(turnLeft,"Left") 
screen.onkey(closeWindow,"Escape")


screen.mainloop()
