import turtle as t


def heart(x, y, col="red"):
    t.up()
    t.goto(x, y)
    t.down()
    t.pencolor(col)
    t.fillcolor(col)
    t.setheading(45)
    t.begin_fill()
    t.fd(140)
    t.circle(70, 180)
    t.rt(90)
    t.circle(70, 180)
    t.fd(140)
    t.end_fill()

t.bgcolor("black")
t.speed(0)
t.ht()

heart(40, -30, "pink")
heart(-10, -100)

t.color("gold")
t.write("Happy Valentine's Day" ,align="center", font=("Times New Roman", 30, "bold italic"))
t.up()
t.goto(-10, 0)
t.color("white")
t.write("I LOVE YOU",align="center", font=("Times New Roman", 20, "bold italic"))

t.done()
