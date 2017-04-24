import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
james = turtle.Turtle()
james.color("black")
james.speed(20)

mom = turtle.Turtle()
mom.color("black")
mom.speed(20)

grace = turtle.Turtle()
grace.color("black")
grace.speed(20)
count = 0
    
def disperseTurtles():
    
    james.left(30)
    mom.left(150)
    grace.left(270)
    james.forward(100)
    mom.forward(100)
    grace.forward(100)

def turtleDance(boxLength):
    #boxLength = 10
    for count in range(50):
        james.color("red")
        mom.color("green")
        grace.color("blue")
        for count in range(2):
            james.forward(boxLength)
            mom.forward(boxLength)
            grace.forward(boxLength)
    
            james.left(150)
            mom.left(150)
            grace.left(150)
    
        #boxLength += 5
        james.left(5)
        mom.left(5)
        grace.left(5)

disperseTurtles()
turtleDance(150)

wn.exitonclick()
