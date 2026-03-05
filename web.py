import turtle as t
import colorsys

t.speed(0)
t.pensize(1)
t.bgcolor('black')

hue = 0

for i in range(160):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(col)
    hue+=0.005
    t.circle(6-i, 90)
    t.lt(80)
    t.circle(6-i, 90)
    t.rt(180)

t.up()
t.goto(0,0)
t.shape("turtle")
t.shapesize(3,3,3)
t.done()
