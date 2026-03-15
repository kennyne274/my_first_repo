import turtle as t
import math
import random

def random_color():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    colors = (r,g,b)
    return colors


t.setup(500, 500)
t.speed(0)
t.pensize(3)
t.bgcolor("ivory")
t.shape("circle")
t.penup()
t.colormode(255)

for hour in range(1, 13):
    angle = 90 - (hour * 30)
    
    x = math.cos(math.radians(angle)) * 150
    y = math.sin(math.radians(angle)) * 150
    
    t.color(random_color())
    t.goto(x, y)
    t.stamp()
    
    text_x = math.cos(math.radians(angle)) * 170
    text_y = math.sin(math.radians(angle)) * 170
    t.goto(text_x, text_y - 10) 
    t.write(f"{hour}", align="center", font=("Arial", 12, "bold"))

t.goto(0, 0)
t.stamp()
t.pendown()
t.setheading(90)
t.pensize(7)
t.forward(110)
t.backward(110)
t.setheading(330)
t.pensize(10)
t.forward(70)
t.ht()

t.done()
