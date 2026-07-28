from turtle import Turtle,Screen
import turtle
from random import choice
colors=["#780000","#c1121f","#03045e","#003049","#004b23","#000000","#a53860","#fb8500"] #Palete of colors
directionToWalk=["forward","backward","right","left"]


def chooseRandomly(list:list) -> str:
    """Choose a element randomly in the list and return it."""
    return choice(list)

def randomWalk(turtle:Turtle,lineTickness:int,steps:int,repetion:int,speed:int,color:str="green"):
    """Draws a random path on the screen."""
    turtle.speed(speed)
    rgbColor=RGBColor()
    for i in range(repetion):
        rgbColor.generateRandomColor()
        #color= chooseRandomly(colors)
        direction=chooseRandomly(directionToWalk)
        turtle.pencolor(rgbColor.color)
        turtle.pensize(lineTickness)
        lineTickness+=0.25

        if direction == "forward":
            turtle.forward(steps)

        elif direction =="backward":
            turtle.backward(steps)

        elif direction == "left":
            turtle.left(90)
            turtle.forward(steps)

        else:
            turtle.left(90)
            turtle.forward(steps)



timmy= turtle.Turtle()
#randomWalk(timmy,2,50,200,"fastest")

#Generating random rgb colors

turtle.colormode(255)
from randomColor import RGBColor
randomWalk(timmy,2,50,200,"fastest")





screen=Screen()
screen.exitonclick()
#screen.delay(25)

