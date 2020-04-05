# Q2. Write a program that draws a hexagon where every 2nd side is a different color, you can set the color to be any
# color of your choice.


import turtle

win = turtle.Screen()
win.setup(.75, .75)
win.bgcolor("black")


#  Define function to draw a hexagon with alternating coloured sides. Will use 'if', and 'elif not' selection statements
# to determine if the position , 'i', in the range(x) is even or odd using the modulo operator. Even elements of the
# range will be red and odd members blue.
def hexagon_creator(self=turtle.Turtle()):  # Have created turtle within the function
    x = 7
    self.setpos(-50, 50)
    for i in range(x):
        self.forward(100)
        self.right(60)
        if i % 2 == 0:
            self.pencolor("red")
        elif not i % 2 == 0:
            self.pencolor("blue")
    self.reset()

def hexagon_creator_2(self=turtle.Turtle()): # Thomás's version
    x = 6
    y = 50
    arc = 360 / x
    for i in range(x):
        if i % 2 == 0:
            self.pencolor("green")
        else:
            self.pencolor("red")
        self.forward(y)
        self.left(arc)
    self.reset()

hexagon_creator()  # Call function to draw hexagon.
hexagon_creator_2()
win.exitonclick()
