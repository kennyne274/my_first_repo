import turtle
turtle.bgcolor("lightyellow")
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.pencolor("teal")


for i in range(80):
    t.forward(i*5)
    t.left(90)

t.up()
t.goto(0,0)
t.down()
turtle.done()
