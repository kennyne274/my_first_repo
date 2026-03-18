

#This Python script uses the turtle module 
#to create a visually striking animation of 100 colorful hexagons rotating on a black background.

import turtle
import random

# Basic setup
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.pensize(1)

# RGB 
turtle.colormode(255)

# drawing hexagon
def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)


for i in range(100):
  
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    t.color(r, g, b)
    
   
    draw_hexagon(100)
    
   
    t.right(3.6)


t.hideturtle()
turtle.done()
