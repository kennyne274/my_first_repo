import turtle as t
import random

t.bgcolor("ivory")
t.setup(width=500, height=400)
t.speed("fastest")
t.colormode(255)
t.hideturtle()

def random_color():
    r = random.randint(70, 250)
    g = random.randint(70, 250)
    b = random.randint(70, 250)
    color = (r,g,b)
    return color

def petal(color):
    t.color(color)
    t.begin_fill()
    t.circle(180, 60)
    t.left(120)
    t.circle(180, 60)
    t.end_fill()

def flower():
    color = random_color()
    angle = 20
    for _ in range(18):
        petal(color)
        t.left(angle)

def center_of_flower():
    t.dot(100, "yellow")
    t.penup()
    t.goto(-5,-34)
    t.setheading(0)

    for _ in range(18):
        t.fd(12)
        t.dot(9, "brown")
        t.left(20)

# drawing a flower
flower()
center_of_flower()

t.exitonclick()
