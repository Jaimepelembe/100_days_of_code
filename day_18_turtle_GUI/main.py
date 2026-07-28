from turtle import Turtle,Screen

colors=["#780000","#c1121f","#03045e","#003049","#004b23","#000000","#a53860","#fb8500"]

def chooseColor(colors:list) -> str:
    """"Choose a color randomly in the colors list and return it."""
    from random import choice

    return choice(colors)


def drawPentagon(turtle:Turtle,size:int,color:str="green",):
    """Draws a pentagon on the screen."""
    sides=5    
    angle = 360.0/sides

    turtle.pencolor(color)

    for i in range(sides):
        turtle.forward(size)
        turtle.right(angle)






timmy= Turtle()

#Change the shape
timmy.shape("turtle")
timmy.color("darkgreen")


def drawSquare(turtle:Turtle,size:int,color:str="blue"):
    """Draws a Square on the screen."""
    turtle.pencolor(color)

    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


def drawIsoscelesTriangle(turtle:Turtle,sides:int,base:int,angleBase:int,angleSides:int,color:str="brown"):
    """Draws a Isosceles Triangle on the screen."""
    turtle.pencolor(color)
    turtle.penup()
    turtle.right(90)
    turtle.pendown()


    turtle.left(angleSides/2)
    turtle.forward(sides)
    angleToReachBase=(360-angleBase*2)/2
    turtle.right(angleToReachBase)
    turtle.forward(base)

    turtle.right(angleToReachBase)
    turtle.forward(sides)




def drawFigure(turtle:Turtle,size:int,sides,color:str="green",):
    """Draws a pentagon on the screen."""    
    angle = 360.0/sides

    turtle.pencolor(color)

    for i in range(sides):
        turtle.forward(size)
        turtle.right(angle)



def drawDashedLine(turtle:Turtle,lineWidth:int,color:str="red",amount:int=50):
    """Draws a dashed line"""

    turtle.pencolor(color)

    for i in range(amount):
        turtle.forward(lineWidth)
        turtle.penup()
        turtle.forward(lineWidth)
        turtle.pendown()




def drawEquilateralTriangle(turtle:Turtle,side:int,color:str="brown"):
    """Draws a equilateral Triangle on the screen."""
    turtle.pencolor(color)

    #turtle.left(angleSides/2)
    for i in range(3):
        turtle.forward(side)
        angle=(360-120)/2
        turtle.right(angle)




def drawFigures(turtle:Turtle, size:int):

    for sides in range(3,11):
        color=chooseColor(colors)
        drawFigure(turtle,size,sides,color)
    
screen=Screen()
screen.delay(25)
drawFigures(timmy,100)
#drawPentagon(myTurtle)
#drawSquare(myTurtle,80)
#drawIsoscelesTriangle(timmy,100,115,55,70)
#drawDashedLine(timmy,10,amount=30)

screen.exitonclick()

