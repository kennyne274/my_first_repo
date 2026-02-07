import turtle
import colorsys

t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.hideturtle()
t.pensize(4)
turtle.tracer(2)

h = 0

for i in range(1500):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+= 0.003
    t.color(c)
    t.left(72)
    for j in range(6):
        t.forward(100)
        t.left(60)
turtle.exitonclick()

