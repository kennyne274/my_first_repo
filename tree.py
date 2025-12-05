import turtle as t
import random

size = 110

# Basic settings
t.bgcolor("black")
t.color("peru")
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()
t.hideturtle()

# Tree drawing function
def tree(i):
    if i < 10:
        return
    else:
        # Draw trunk/branch
        t.pensize((i/12))
        t.forward(i)
      
        angle = random.uniform(20, 35)
        length = random.uniform(0.7, 0.85)

        # Left branch
        t.left(angle)
        tree(i * length)

        # Right branch
        t.right(angle * 2)
        tree(i * length)

        # Return to previous branch position
        t.left(angle)
        t.backward(i)

tree(size)
t.done()
    