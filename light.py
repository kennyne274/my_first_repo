import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.pensize(2)

for i in range(100):
    t.color(0,i/100,i/100)
    for _ in range(6):
        t.forward(100)
        t.right(60)
    t.right(3.6)
t.hideturtle()
turtle.done()

