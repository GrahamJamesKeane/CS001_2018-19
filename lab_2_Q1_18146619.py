# Graham Keane 18146619 CS001 Lab 2 Question 1

# Question 1: Write a program that imports the turtle library and creates a Turtle & Screen that draws a rectangle.
# Set the background colour to black, the line colour to white and the pen size to 5


# Import the Turtle Library
import turtle

# Graphics window with background colour black
from turtle import Turtle

win = turtle.Screen()
win.bgcolor("black")
win.title("Lab 2 Question 1")

# Create a Turtle object "A" with a white line colour and pen size of 5
A: Turtle = turtle.Turtle()
A.color("white")
A.pensize(5)

# Draw a rectangle with Turtle object A
A.penup()
A.goto((-200), (-100))
A.pendown()

# Use a for-loop to move "A". A for loop reduces the amount of writen code needed to produce a result:
for i in range(2):
    A.forward(400)
    A.left(90)
    A.forward(200)
    A.left(90)

# Graphics window exit
win.exitonclick()
