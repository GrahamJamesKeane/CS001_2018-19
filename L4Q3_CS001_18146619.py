# Q3. Write a program that uses a function to create the following shape found in your notes:


import turtle

win = turtle.Screen()
win.setup(.75, .75)
win.bgcolor("black")


# Creates a function that draws polygons by increasing number of sides, from 3 to 12, or from a triangle to Dodecagon
def cool_polygons(shredder=turtle.Turtle()):
    shredder.setposition(-50, -200)
    shredder.shape("circle")
    for i in range(3, 12):
        x = i
        y = 150  # unit distance
        if x % 3 == 0:  # colour shifting by modulo
            shredder.color("green")
            shredder.fillcolor("purple")
        elif x % 2 == 0:
            shredder.color("blue")
            shredder.fillcolor("yellow")
        elif x % 5 == 0:
            shredder.color("yellow")
            shredder.fillcolor("red")
        else:
            shredder.color("red")
            shredder.fillcolor("white")
        for j in range(x):  # actual polygon routine
            shredder.forward(y)
            shredder.left(360 / x)


cool_polygons()  # Call the function to draw the polygons

win.exitonclick()
