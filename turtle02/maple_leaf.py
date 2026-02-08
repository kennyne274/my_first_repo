# Drawing maple_leaf

from turtle import *
import colorsys

bgcolor("black")
speed(0)
hideturtle()
tracer(2)


h = 0
n = 180
for i in range(n):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.0012
        color(c)
        circle(180-i, 90)
        left(100)
        circle(180-i, 90)
        right(80)
      

done()
