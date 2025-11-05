import turtle as t
import random

# set up the drawing environment
t.bgcolor("cornsilk") # Set background color
t.colormode(255)      # Use RGB color mode
t.speed(0)            # Set turtle speed to the fastest
t.penup()             # Lift the pen to avoid drawing lines
t.hideturtle()        # Hide the turtle icorn 

# Move the turtle to the starting position
t.setheading(225)
t.forward(300)
t.setheading(0)

# Total number of dots to draw
num_dots = 100 

# Draw a 10 X 10 grid of colorful dots
for i in range(1,num_dots + 1):
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,255)
    t.dot(20, (r, g, b))
    t.forward(50)
# After every 10 dots, move up to the next row
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


t.done()

