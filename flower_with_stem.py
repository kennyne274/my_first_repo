import turtle as t
import time

t.bgcolor("black")
t.speed(0)
t.hideturtle()

def draw_stem(x, y, height=35):
    size = height
    t.penup()
    t.goto(x, y)         
    t.pendown()
    t.color("#228B22")      
    
    for i in range(0, height): 
        t.seth(90)  
        t.fd(10)
        t.pensize(size)
        time.sleep(0.02)   
        size -= 1     


def draw_leaf(x, y, angle, height=32):
    size = height *2
    t.penup()
    t.goto(x, y)          # 시작 위치 (화면 아래)
    t.pendown()
    t.color("#228B22")      
    
    for j in range(0, height): 
        t.seth(angle)  
        t.fd(7)
        t.pensize(size)
        time.sleep(0.02)   
        size -= 2     

def draw_petal(col): 
    t.color(col)
    t.begin_fill()
    t.circle(150, 60)
    t.left(120)
    t.circle(150, 60)
    t.left(120)
    t.end_fill()

def draw_flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for f in range(20):
        colors = ["#FF1493", "#FF69B4", "#F43776", "#FF4D94"]
        draw_petal(colors[f % len(colors)])
        t.left(18)

    # flower center
    t.penup()
    t.goto(x, y)
    t.dot(120, "yellow")

    t.goto(x, y)
    t.pendown()
    center()


def center():
    t.color("#B94902")
    for c in range(30):
        t.circle(30)
        t.right(12)


draw_stem(0, -330)
draw_leaf(20, -340, 40, 32)
draw_leaf(-20, -340, 140, 32)
draw_flower(0, 10)

t.done()
