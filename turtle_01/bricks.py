import turtle as t


def draw_square(square_size, col):
    t.begin_fill()
    t.color("black", col)
    for i in range(4):
        t.fd(square_size)
        t.lt(90)
    t.end_fill()


t.setup(800,600)
w, h = 800, 600
num = 5
square_size = w / num
x, y = -w/2 - square_size, h/2 -square_size

t.bgcolor("black")
t.pensize(12)
t.speed(0)
t.colormode(255)
t.ht()
t.penup()
t.goto(x, y)
t.pendown()

step = 7
for j in range(step):
    for c in range(num):
        colors = ["#f79707",  "#f70707", "#ffffff", "#f75707", "brown", "#f76b07", "#f7b307"]
        col = colors[c % len(colors)]
        t.seth(0)
        t.fd(square_size)    
        draw_square(square_size, col)
    num += 2
    square_size = w / num
    t.seth(270)
    t.fd(square_size) 
    t.seth(180)
    t.fd(w - square_size/4)

t.done()
