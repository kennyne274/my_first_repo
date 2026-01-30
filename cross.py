
# Draw a cross symbol

from turtle import *

shape("turtle")

bgcolor("#000000")
pencolor("crimson")
pensize(30)

forward(200)
home()

backward(200)
home()

setheading(90)
forward(200)
home()
setheading(270)
forward(200)

setheading(0)
circle(200)

hideturtle()
done()
