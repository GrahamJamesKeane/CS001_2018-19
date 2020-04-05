# Graham Keane 18146619
# Question 4: Write a program that produces the following shape (Ten circle for loop).

# Import the turtle module.
import turtle

# Create graphics window:
win = turtle.Screen()
win.screensize(200, 200, "black")
win.title("Lab 3 Question 4")

# Create turtle "don":
don = turtle.Turtle()
don.setpos(-50, -50)
don.speed("fast")
don.pencolor("blue")
don.pensize(2)
don.shape("circle")

# Create turtle raph:
raph = turtle.Turtle()
raph.setpos(-50, -50)
raph.speed("fast")
raph.pencolor("red")
raph.pensize(2)
raph.shape("circle")

# Draw compound circle
x = 10  # iterations of i to draw circles:
for i in range(x):
    don.left(360 / x)   # Changes heading to begin next circle
    raph.right(360 / x)
    for j in range(1):
        don.circle(50, 360, 36)
        raph.circle(50, 360, 36)

# Exit graphics window
win.bye()
