# Drawing the rainbow

import turtle as t

t.bgcolor("skyblue")
t.title("The Rainbow")
t.pensize(15)
t.hideturtle()

x =200
y =-50

colors = ["Red", "orange", "yellow", "green", "blue", "navy", "purple"]

t.setheading(90)
t.penup()
t.goto(x,y)
t.pendown()

radius = 200

for col in colors:
    t.setheading(90)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.circle(radius, 180)
    radius -= 14
    x -= 14

t.done()

