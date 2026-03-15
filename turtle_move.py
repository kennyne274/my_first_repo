import turtle as t
import random
import math

def create_turtle():
    global turtles
    turtles = []

    for i in range(60):
        tt = t.Turtle()
        tt.shape("turtle")
        tt.shapesize(1.5)
        tt.color(random_color())
        tt.penup()
        angle = i * 10
        tt.goto(math.cos(math.radians(angle)) * 120,
                math.sin(math.radians(angle)) * 120)
        tt.setheading(angle + 90)
        turtles.append(tt)

def random_color():
    r = random.randint(70, 250)
    g = random.randint(70, 250)
    b = random.randint(70, 250)
    colors = (r,g,b)
    return colors


def move():
    for tt in turtles:
        tt.right(random.uniform(-15, 15))
        tt.forward(random.uniform(3, 8))
        tt.left(random.uniform(-20, 20))
        
        if random.random() < 0.04:
            tt.color(random_color())
    
    t.update()
    t.ontimer(move, 80)


t.bgcolor("black")
t.tracer(0)
t.colormode(255)

create_turtle()
move()
t.done()
