
import turtle as t

colors =["red","yellow","blue"]
t.bgcolor("black")
t.speed(0)
t.hideturtle()
i = 0
while True:
    t.color(colors[i%3])
    t.forward(i)
    t.lt(118)
    i += 1
    if i == 1000:
        break


t.done()
