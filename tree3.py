from turtle import *


setup(600, 600)
title("Tree")
bgcolor("#0A022B")   
color("#74A4FC")
pensize(3)
speed(0)

# drawing a tree

def tree(size, level, angle):
    if level == 0:
        color("white")
        dot(size)
        color("brown")
        return
    forward(size)

    # right branch
    right(angle)
    tree(size*0.8, level-1, angle)
    
    # left branch
    left(angle*2)
    tree(size*0.8, level-1, angle)
    right(angle)
    backward(size)

setheading(90)
penup()
goto(0,-120)
pendown()
tree(90,6,30)

hideturtle()

done()

