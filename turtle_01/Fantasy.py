import turtle
import colorsys

t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.hideturtle()
turtle.tracer(2)

h = 0

for i in range(1000):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+= 0.003
    t.color(c)
    t.left(149)
    for j in range(5):
        t.forward(200)
        t.left(144)
turtle.exitonclick()

