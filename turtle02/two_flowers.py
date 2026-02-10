import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(10)
t.pensize(1)
t.hideturtle()


def flower(x,y, num):
    h = 0
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(300):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.pencolor(c)
    
        for j in range(2):

            t.circle(100-i/3,180)
            t.lt(100)
        h += num
           
flower(40,40,0.005)
flower(-120,0,0.0072)

t.update()
t.done()
