# Graham Keane 18146619
# Question 1: Write a program that uses a for loop to create a regular pentagon with each side being 80
# units in length.

# Import turtle module:
import turtle

# Create graphics window:
win = turtle.Screen()
win.screensize(200, 200, "black")
win.title("Lab 3 Question 1")

# Create turtle "don":
don = turtle.Turtle()
don.setpos(-100, -100)
don.pencolor("red")
don.pensize(2)
don.shape("circle")

# Draw a regular pentagon:
x = 5  # iterations of x that will draw a line y units long:
y = 80
for i in range(x):
    don.forward(y)
    don.left(360 / x)

# Exit graphics window
win.exitonclick()
