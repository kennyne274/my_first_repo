
import turtle as t
import random

size = 120
# Basic settings
t.bgcolor("black")
t.colormode(255)
t.speed(0)
t.setheading(90)
t.penup()
t.goto(0, -250)
t.pendown()
t.hideturtle()

def tree(i):
    if i < 10:
        return
    # Tree drawing function
    x = random.randint(50,255)
    y = random.randint(50,255)
    z = random.randint(50,255)
    shrink·ratio = random.uniform(0.65,0.85)
    angle = random.uniform(25,35)
    t.pensize(i/12)
    t.pencolor(x,y,z)
    t.forward(i)

    # Left branch
    t.left(angle)
    tree(i*shrink·ratio)

    # Right branch
    t.right(angle*2)
    tree(i*shrink·ratio)

    # Return to previous branch position
    t.left(angle)
    t.backward(i)


tree(size)
t.done()

