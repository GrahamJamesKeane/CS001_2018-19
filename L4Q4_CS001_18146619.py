# Q4. Write a program that draws the following shape and uses a pentagon() function to create the pentagons:

import turtle
from random import randint

# Create a graphics window:
win = turtle.Screen()
win.setup(.75, .75)
win.bgcolor("black")

# Create a turtle:
shredder = turtle.Turtle()


# Create a function to initialise the turtle when it is called inside a function:
def shredder_int():
    shredder.penup()
    shredder.setposition(-50, 50)
    shredder.speed("fast")
    shredder.shape("turtle")
    shredder.pensize(3)
    shredder.pendown()


# Create function to draw a series of pentagrams that trace a square about their centre.
def pentagon_creator():
    x = 4  # Inner-arc traced by pentagons
    z = 5  # Arc of pentagons
    y = 100  # Unit length
    shredder_int()
    w = randint(1, 30)  # Randint for colour selections statements:
    for j in range(3, 9):
        if w % 2 == 0:  # Colour selection statements
            shredder.color("red")
            shredder.fillcolor("blue")
        elif w % 3 == 0:
            shredder.color("blue")
            shredder.fillcolor("red")
        else:
            shredder.color("green")
            shredder.fillcolor("purple")
    for k in range(x):  # Pentagon drawing routine
        shredder.forward(100)
        shredder.right(360 / x)
        for i in range(z):
            shredder.forward(y)
            shredder.left(360 / z)


pentagon_creator()  # Call to run function defined above

win.exitonclick()  # exit graphics window
