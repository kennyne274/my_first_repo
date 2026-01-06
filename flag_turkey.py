# Flag of Turkey 

import turtle as t

# Setup
t.speed(0)
t.bgcolor("black")
t.hideturtle()

# draw the red flag
t.penup()
t.goto(-220, -120)
t.pendown()
t.color("#E30A17")
t.begin_fill()
for _ in range(2):
    t.forward(420)
    t.left(90)
    t.forward(280)
    t.left(90)
t.end_fill()

# draw the moon
# first circle
t.penup()
t.goto(-90, -50)
t.color("white")
t.begin_fill()
t.circle(70)  
t.end_fill()

# second cirle
t.penup()
t.goto(-70, -40)
t.color("#E30A17")
t.begin_fill()
t.circle(60)  
t.end_fill()

#draw the star
t.penup()
t.goto(-50, 20)
t.setheading(20)
t.color("white")
t.begin_fill()
for _ in range(5):
    t.forward(55)
    t.right(144)
t.end_fill()

t.done()
