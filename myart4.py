import turtle as t
import random

t.bgcolor("cornsilk")
t.colormode(255)
t.speed(0)
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)

num_dots = 100

for i in range(1,num_dots + 1):
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,255)
    t.dot(20, (r, g, b))
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


t.done()