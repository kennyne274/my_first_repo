import turtle as t

t.speed(1)

t.bgcolor("black")
t.penup()
t.goto(-60, 60)
t.pendown()
t.color('#00adef')
t.begin_fill()

t.goto(90, 100)
t.goto(90, -100)
t.goto(-60, -60)
t.goto(-60, 60)
t.end_fill()

t.color("black")
t.goto(5, 100)
t.width(10)

t.goto(5, -100)
t.penup()
t.goto(100, 0)
t.pendown()
t.goto(-100, 0)

t.done()

