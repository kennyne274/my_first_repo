import turtle as t
import random

t.bgcolor("ivory")
t.speed(0)

t.penup()

x = -300
y = -270

t.goto(x, y)
t.pendown()
t.colormode(255)

def draw_dots(size):
    global y
    for i in range(10):    
        for j in range(11):
            r = random.randint(50, 250)
            g = random.randint(50, 250)
            b = random.randint(50, 250)
            t.color(r,g,b)
            t.dot(size)
            t.penup()
            t.fd(size*2)          

        y += size*2

        t.goto(x, y)
      

draw_dots(30)

t.hideturtle()

t.done()
