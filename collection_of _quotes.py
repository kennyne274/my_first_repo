# This code is good for kids. It's also beneficial for lazy teachers

import turtle as t
import random

text = [
        "Where there is a will, there is a way.",
        "Learn from yesterday, live for today, hope for tomorrow.",
        "Don’t cry because it’s over, smile because it happened.",
        "All you need is love.", 
        "To thine own self be true.",
        "No pain, no gain",
        "The best is yet to come.",
        "Honesty is the best policy.",
    ]


def random_color():
    r = random.randint(70, 250)
    g = random.randint(70, 250)
    b = random.randint(70, 250)
    colors = (r,g,b)
    return colors

t.shapesize(3)
t.setheading(90)
t.speed(2)
t.bgcolor("black")
t.colormode(255)
t.shape("turtle")
t.color("gold")
t.penup()
t.goto(0, -300)

for i in range(len(text)):
    t.write(text[i], align="center", font=("Times New Roman", 20, "bold"))
    t.color(random_color())
    t.fd(70)

tt = t.Turtle()
tt.ht()
tt.speed(0)

for i in range(50):
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    size = random.uniform(2, 6)
    tt.up()
    tt.goto(x, y)
    tt.dot(size, "white")

t.done()
