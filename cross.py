# Draw a cross symbol

from turtle import *

def cross(size):
    shape("turtle")

    bgcolor("#000000")
    pencolor("crimson")
    pensize(15)

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

cross(100)
hideturtle()

penup()
goto(0,- 100)
color("#F9E106")
write("Jesus Christ loves you!", align="center", font=("Arial", 20, "italic"))

done()
