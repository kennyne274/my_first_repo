# Simple and pretty flower

import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(10)
t.pensize(1)
t.hideturtle()
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
 
    for j in range(2):

        t.circle(30+i/2,160)
        t.lt(100)
   
    h += 0.0058
    
t.done()
