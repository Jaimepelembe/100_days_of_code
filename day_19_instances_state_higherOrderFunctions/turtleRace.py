from turtle import Turtle,Screen



def closeWindow():
    screen.bye()



timmy=Turtle()
tommy=Turtle()
leonardo=Turtle()

rafael=Turtle()
michelangelo=Turtle()
donatello=Turtle()
turtles=[leonardo,rafael,michelangelo,donatello,timmy,tommy]
colors=["blue","red","orange","purple","yellow","green"]

def setTurtles(turtles:list[Turtle],colors:list[str]):
    """Set up the turtles in their initial position and give them the colors."""

    y=-100
    x=-360

    for i, turtle in enumerate(turtles):
        turtle.penup()
        turtle.shape("turtle")
        turtle.color([colors[i]])
        turtle.goto(x,y)
        y+=50



def moveTurtles(turtles:list[Turtle]):
    from random import randint

    for turtle in turtles:
        distance=randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() >=400-20: # A turtle has 40 pixels of width 
            if turtle.color() == userChoose:
                print("You win the race. Congratulations")
            else:
                print(f"You lose the race. The winner is {turtle.color()[0]} Turtle")
            return True



screen=Screen()
screen.setup(width=800,height=600)

continuePlaying=True

while continuePlaying:
    userChoose=screen.textinput("Make your bet","Choose a Turtle color: blue, red, orange, purple, yellow or green: ")
    setTurtles(turtles,colors)

    gameOver=False
    while not gameOver:
        gameOver=moveTurtles(turtles)

    
    userAnswer=screen.textinput("Game Over","Do you want to play again? Press 'y' or 'n': ")

    if userAnswer == "n":
        continuePlaying=False
        closeWindow()



screen.listen()
screen.onkey(closeWindow,"Escape")


screen.mainloop()
