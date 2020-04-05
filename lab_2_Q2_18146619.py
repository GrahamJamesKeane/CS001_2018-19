# Graham Keane 18146619 CS001 Lab 2 Question 2:

# Question 2: Write a program that imports the turtle library and creates a Turtle and Screen that draw an equilateral
# triangle. Set the background colour to purple and the line colour to brown.

# Import the Turtle Library:
import turtle

# Graphics window with purple background colour and title:
from turtle import Turtle

win = turtle.Screen()
win.bgcolor("purple")
win.title("Lab 2 Question 2")

# Create a Turtle object "B" with a brown line colour.
B: Turtle = turtle.Turtle()
B.color("brown")

# Draw an equilateral with Turtle object B. An equilateral triangle has three identical angles of (180/3)= 60 degrees
# Therefore, we will change the heading of Turtle B by 120 degrees at each point in the triangle after first moving
# forward from the point of origin by 400 units. This will draw out an equilateral triangle with sides of 400 units.

B.penup()
B.goto((-200), (-100))
B.pendown()

# Use a for-loop to move "B":
for i in range(3):
    B.forward(400)
    B.left(120)

# Graphics window exit
win.exitonclick()
