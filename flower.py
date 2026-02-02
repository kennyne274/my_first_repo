from turtle import *


bgcolor("black")
speed(0)
hideturtle()


colors = ["yellow", "orange"]


n = 100
for i in range(n):
    for col in colors:
        color(col)
        circle(180-i, 95)
        left(90)
        circle(180-i, 95)
        right(60)

done()

