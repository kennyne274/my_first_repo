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

for i in range(10):    
    for j in range(11):
        r = random.randint(50, 250)
        g = random.randint(50, 250)
        b = random.randint(50, 250)
        t.color(r,g,b)
        t.dot(30)
        t.penup()
        t.fd(60)
        t.pendown()
       

    y += 60

    t.penup()
    t.goto(x, y)
    t.pendown()

t.hideturtle()

t.done()
