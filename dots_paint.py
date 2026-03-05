import turtle as t

t.setup(width=400, height=400)
t.bgcolor("aliceblue")
t.colormode(255)
t.speed(0)
t.hideturtle()

num_dots = 100

def dots():
    for i in range(1, num_dots+1):
        r = 0 + i
        g = int(0 + i * 2.5)
        b = 255-r
        t.color(r,g,b)
        t.setheading(0)
        t.dot(25)
        t.fd(25)
        if i % 10 == 0:
            t.setheading(90)
            t.fd(25)
            t.setheading(180)
            t.fd(250)
            
x = -110
y = -110
t.penup()
t.goto(x,y)          

dots()
t.exitonclick()
