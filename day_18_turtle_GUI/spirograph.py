import turtle
from randomColor import RGBColor



def drawSphirograph(turtle:turtle.Turtle,radius:int,angle:int,speed:str="normal"):
    """"Draws a Sphirograph"""
    turtle.speed(speed)
    rgbColor=RGBColor()

    for i in range(int(360/angle)):
        rgbColor.generateRandomColor()
        turtle.pencolor(rgbColor.color)
        turtle.circle(radius)
        turtle.setheading(turtle.heading()+angle) # or turtle.left(angle)
        


timmy=turtle.Turtle()
turtle.colormode(255)

drawSphirograph(timmy,100,5,"fastest")

screen=turtle.Screen()
screen.exitonclick()