# Graham Keane 18146619
# Question 3: Write a program that uses a for loop to create a six sided asterisk (star symbol on your
# keyboard) with each line being 50 units of length from the centre.

# Import the turtle module.
import turtle

# Create graphics window:
win = turtle.Screen()
win.screensize(200, 200, "black")
win.title("Lab 3 Question 3")

# Create turtle "don":
don = turtle.Turtle()
don.setpos(-50, -50)
don.hideturtle()
don.speed("slow")
don.pencolor("blue")
don.pensize(5)
don.shape("circle")

# Draw a six point asterisk using a for-loop with unit lengths of 50 from the centre:
x = 6  # number of points
d = 50  # unit length
for i in range(x):
    don.forward(d)
    don.left(360 / x)
    don.backward(d)

# Exit graphics window
win.exitonclick()
