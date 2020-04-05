# Graham Keane 18146619 CS001 Lab 2 Question 5:

# Question 5: Write a program that creates a square and then a circle inside that fits perfectly. You should also change
# the background colour and the shape of the turtle:

# Import the turtle module:
import turtle

#  Create graphics window with black background, and a title:
win = turtle.Screen()
win.bgcolor("black")
win.title("Lab 2 Question 5")

# Create turtle "F":
F = turtle.Turtle()
F.color("red")
F.pensize(10)
F.shape("circle")
F.penup()
F.goto(200, -200)
F.pendown()

# Draw a square using a for-loop:
for i in range(4):
    F.back(400)
    F.right(90)

F.penup()
F.setpos(0, -200)
F.shape("square")
F.color("blue")
F.pendown()

# Draw a circle that fits perfectly inside the square. Given a square side length of 400 pixels, then the radius of the
# circle must be 200:
F.circle(200, 360, 36)
F.fillcolor("red")

# Just messing around with the undo function. It looks cool!
for r in range(14):
    F.undo()

F.hideturtle()

# Exit graphics window:
win.bye()
