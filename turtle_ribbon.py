

import turtle as t

t.bgcolor("black")
t.speed(0)
t.hideturtle()

t.color("cyan")


colors = ["white", "cyan"]

def petal():
    for _ in range(2):
        t.circle(200, 60)
        t.lt(120)


def spiral(turn):

    for i in range(28):
        t.color(colors[i % len(colors)])
        petal()
        t.lt(turn)



spiral(121)
t.setheading(0)
spiral(-121)

t.done()
