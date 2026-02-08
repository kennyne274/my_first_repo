from turtle import *
import colorsys

bgcolor("black")
speed(0)
hideturtle()
tracer(2)


h = 0
n = 800
for i in range(n):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    fd(i * 0.7)
    circle(i*0.2)
    backward(i*0.7)
    left(80)
    
    
done()
