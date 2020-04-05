# Graham Keane 18146619 CS001 Lab 2 Question 3:

# Question 3: Write a program that imports the turtle library and creates a Turtle and Screen that draws a square.
# Set the background colour to blue and the line colour to white.

# Import the Turtle Library:
import turtle

# Graphics window with black background colour and title:
from turtle import Turtle

win = turtle.Screen()
win.bgcolor("blue")
win.title("Lab 2 Question 3")

# Create turtle "C" with a white line colour:
C: Turtle = turtle.Turtle()
C.color("white")

# Draw a square with "C":
C.penup()
C.goto((-200), (-200))
C.pendown()

# Use a for loop to move "C":
for i in range(4):
    C.forward(400)
    C.left(90)

# Undo:
for j in range(8):
    C.undo()

# Graphics window exit
win.bye()
