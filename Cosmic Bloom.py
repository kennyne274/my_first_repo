# Cosmic Bloom

import turtle as t

t.bgcolor("black")
t.pensize(1)
t.speed(0)
t.hideturtle()

colors = ["orange", "coral","ivory"]

for i in range(36):
    t.goto(0,0)
    t.forward(120)
    t.right(69)
    t.color(colors[i % 3])
    for j in range(4):
       t.forward(i*5)
       t.circle(i*1.5)
      
t.done()
