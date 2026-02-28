import turtle as t
import random

"""It's another way of drawing dots. 
I have been studying Python for 5 months. 
I'm not a good student. I want someone to give me advice"""

# Total number of dots to draw
num_dot = 100

def random_color():
    r = random.randint(50, 250)
    g = random.randint(50, 250)
    b = random.randint(50, 250)
    colors = (r,g,b)
    return colors

def draw_dots():
    for i in range(1, num_dot+1):
        t.setheading(0)
        t.dot(25, random_color())
        t.fd(65)
        
        if i % 10 == 0:
            t.setheading(90)
            t.fd(60)
            t.setheading(180)
            t.fd(650)


t.bgcolor("ivory")
t.speed(0)
t.penup()

x = -300
y = -270

t.goto(x, y)
t.colormode(255)
draw_dots()
t.hideturtle()

t.done()
