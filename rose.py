#Creating a pink rose

import turtle as t

t.bgcolor("black")
t.speed(0)

colors = ["pink", "hotpink"]

for i in range(200):
    t.color(colors[i%2])
    t.pensize(i /50)
    t.forward(i)
    t.left(65)

t.hideturtle()
t.done()
