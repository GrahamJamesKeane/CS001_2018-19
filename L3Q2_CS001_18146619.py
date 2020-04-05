# Graham Keane 18146619
# Question 2: Write a program that produces the following shape (Ten Square for loop).

# Import the turtle module.
import turtle

# Create graphics window:
win = turtle.Screen()
win.screensize(200, 200, "black")
win.title("Lab 3 Question 2")

# Create turtle "don":
don = turtle.Turtle()
don.setpos(-50, -50)
don.speed("fast")
don.pencolor("blue")
don.pensize(2)
don.shape("circle")

# Create turtle "raph":
raph = turtle.Turtle()
raph.setpos(-50, -50)
raph.speed("fast")
raph.pencolor("red")
raph.pensize(2)
raph.shape("circle")

# Draw compound design using uniform square outlines:
x = 10  # iterations of drawing the square routine:
y = 4  # number of sides in shape
for i in range(x):  # Rotates the turtles
    don.right(360 / x)
    raph.left(360 / x)
    for j in range(y):  # Creates the squares
        don.forward(100)
        don.right(360 / y)
        raph.backward(100)
        raph.left(360 / y)

# Undo the design
for l in range(100):
    don.undo()
    raph.undo()
# Exit graphics window
win.bye()
