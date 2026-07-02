import turtle
import colorsys

t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.shape("turtle")

h = 0

t.penup()
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+= 0.007
    t.color(c)
    t.stamp()
    t.forward(i+12)
    t.left(25)


turtle.exitonclick()

