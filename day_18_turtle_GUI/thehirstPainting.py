# Install colorgram
 #pip install colorgram.py

import colorgram
import turtle
from random import choice

def extractColors(fileName:str,numberColors:int)-> list:
    """Extracts a certain number of colors from an image. Returns a list of RGB and HSL tuples"""
    listColors=colorgram.extract(fileName,numberColors)
    
    return listColors

def getListOfRgbTuples(listOfColors)->list:
    """"Returns a list of RGB tuples representing the colors."""
    listOfTuples=[]
    for color in listOfColors:
        red=color.rgb[0]
        green=color.rgb[1]
        blue=color.rgb[2]
        listOfTuples.append((red,green,blue))
        
    return listOfTuples
   

fileName="damien_hirst_spots.jpg"
colorsExtracted= extractColors(fileName,10) 
listColors=getListOfRgbTuples(colorsExtracted) #[(252, 250, 247), (253, 247, 250), (237, 252, 245), (249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70)]




def chooseRandomly(list:list) -> str:
    """Choose a element randomly in the list and return it."""
    return choice(list)

def drawDots(turtle:turtle.Turtle,colors:list,lines:int,radius:int=20,space:int=50,speed:str="normal" ):
    """"Draws dots on the screen. Following the Damien Hirst pattern"""
    turtle.speed(speed)
    turtle.penup()
    turtle.setposition(0,-4*space) # Put the turtle in a position where we can draw all the dots in the visible area of the screen

    for i in range(lines):
        for j in range(lines):
            turtle.pendown()
            color=chooseRandomly(colors)
            #turtle.fillcolor(color)

            turtle.dot(radius,color)
            turtle.penup()
            turtle.forward(space)
            

        # Jump to another column    
        x,y=turtle.position()
        x=0
        y=y+space
        turtle.setposition(x,y)


turtle.colormode(255)
timmy = turtle.Turtle()

drawDots(timmy,listColors,10,20,50,"fast")

screen = turtle.Screen()
screen.exitonclick()
