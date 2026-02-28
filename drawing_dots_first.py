

import turtle as t
import random

def random_color():
    r = random.randint(50, 250)
    g = random.randint(50, 250)
    b = random.randint(50, 250)
    colors = (r,g,b)
    return colors

def draw_dots(size, row=10, col=11):
    global y
    for i in range(row):    
        for j in range(col):
            t.color(random_color())
            t.dot(size)
            t.penup()
            t.fd(size*2)          

        y += size*2

        t.goto(x, y)


t.bgcolor("ivory")
t.speed(0)
t.penup()

x = -300
y = -270

t.goto(x, y)
t.colormode(255)

draw_dots(30)

t.hideturtle()

t.done()
