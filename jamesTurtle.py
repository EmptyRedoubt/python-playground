import turtle
wn = turtle.Screen()
james = turtle.Turtle()
count = 0
boxLength = 10

while (count < 10):
    count += 1
    count2 = 0
    while (count2 < 2):
        james.forward(boxLength)
        james.left(90)
        count2 += 1

    boxLength += 5
    james.forward(boxLength)
    james.left(90)
    james.forward(boxLength)

wn.exitonclick()
