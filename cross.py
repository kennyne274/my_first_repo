
# Draw a cross symbol

from turtle import *

def cross(size):
    shape("turtle")

    bgcolor("#000000")
    pencolor("crimson")
    pensize(30)

    forward(size)
    home()

    backward(size)
    home()

    setheading(90)
    forward(size)
    home()

    setheading(270)
    forward(size)

    setheading(0)
    circle(size)

cross(180)
hideturtle()

done()
