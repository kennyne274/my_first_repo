import turtle as t
import random

# A tree and field with snow. I like this code. 

# tree
def draw_branch(length, angle, level):
    if level == 0:
        return 
   
    t.pensize(level * 1.5)
    if level > 4:
        t.pencolor("brown")     
    elif level > 2:
        t.pencolor("sandybrown")
    else:
        t.pencolor("green") 
    
    t.forward(length)   
 
    t.right(angle)   
    draw_branch(length * 0.7, angle, level - 1)
  
    t.left(angle * 2)
    draw_branch(length * 0.7, angle, level - 1)
    
    t.right(angle)
    t.backward(length)


def snow(num=300):
    # snow
    t.pencolor("snow")
    t.penup()
    t.goto(-400, -280)

    for _ in range(num):
        x = random.randint(-400, 400)
        y = random.randint(-280, -220)
        t.goto(x, y)
        t.dot(random.randint(4, 12))

def field(): 
    # field
    t.setheading(0)
    for _ in range(20):
        t.dot(120)
        t.fd(30)
    t.setheading(180)
    for _ in range(40):
        t.dot(120)
        t.fd(30)
    snow()

# basic set up
t.bgcolor("ivory")  
t.tracer(2)       
t.penup()
t.goto(0, -280)
t.pendown()
t.left(90)         

# drawing a tree
draw_branch(140, 30, 11)   
field()

t.exitonclick()
