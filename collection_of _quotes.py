import turtle as t
import random

# This code is really a good practice piece for kids. It's also beneficial for lazy teachers

text = [
        "Where there is a will, there is a way.",
        "Learn from yesterday, live for today, hope for tomorrow.",
        "Don’t cry because it’s over, smile because it happened.",
        "All you need is love.", 
        "To thine own self be true.",
        "Where there is a will, there is a way.",
        "The best is yet to come.",
        "Honesty is the best policy.",
    ]

def random_color():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    colors = (r,g,b)
    return colors
    
t.shapesize(3)
t.setheading(90)
t.bgcolor("cornsilk")
t.colormode(255)
t.shape("turtle")
t.color("gold")
t.penup()
t.goto(0, -300)

for i in range(8):
    t.write(text[i], align="center", font=("Times New Roman", 21, "bold italic"))
    t.color(random_color())
    t.fd(70)

t.done()import turtle as t
import random

text = [
        "Where there is a will, there is a way.",
        "Learn from yesterday, live for today, hope for tomorrow.",
        "Don’t cry because it’s over, smile because it happened.",
        "All you need is love.", 
        "To thine own self be true.",
        "Where there is a will, there is a way.",
        "The best is yet to come.",
        "Honesty is the best policy.",
    ]

def random_color():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    colors = (r,g,b)
    return colors
    
t.shapesize(3)
t.setheading(90)
t.bgcolor("cornsilk")
t.colormode(255)
t.shape("turtle")
t.color("gold")
t.penup()
t.goto(0, -300)

for i in range(8):
    t.write(text[i], align="center", font=("Times New Roman", 21, "bold italic"))
    t.color(random_color())
    t.fd(70)

t.done()
