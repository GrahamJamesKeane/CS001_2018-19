# Graham Keane 18146619 CS001 Lab 2 Question 4:

# Question 4: Write a program that creates two turtles. Let one draw a triangle in pink and the other draw a box
# around the triangle in blue. You should also change the background colour and shape of the turtle.

# Import the Turtle Library
import turtle

# Graphics window with black background and title:
from turtle import Turtle

win = turtle.Screen()
win.bgcolor("black")
win.title("Lab 2 Question 4")

# Create a triangle shape with "D" using a pink line colour:
D = turtle.Turtle()
D.hideturtle()
D.color("pink")
D.pensize(5)
D.shape("triangle")

# Create a square shape with "E" using a blue line colour:
E: Turtle = turtle.Turtle()
E.hideturtle()
E.color("blue")
E.pensize(5)
E.shape("square")

# Draw a triangle with "D":
D.pensize(10)
D.penup()
D.goto((-200), (-150))
D.pendown()
D.settiltangle(180)

# Use a for-loop to to move "D":
i: int
for i in range(3):
    D.forward(400)
    D.left(120)

# Draw a square, which encloses the triangle drawn by "D", with "E":
E.pensize(10)
E.penup()
E.goto((-225), (-203.6))
E.pendown()

# Use a for-loop to move "E":
j: int
for j in range(4):
    E.forward(450)
    E.left(90)

# Undo all moves:
for e in range(14):
    E.undo()
    D.undo()

# Graphics window exit on completion of program:
win.bye()
