import turtle
import colorsys

t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.hideturtle()
turtle.tracer(10)

h = 0

for i in range(1500):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+= 0.005
    t.color(c)
    t.left(72)
    for j in range(5):
        t.forward(i*6)
        t.left(115)
turtle.exitonclick()

