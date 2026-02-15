
import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.colormode(255)


t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# drawing the blue Sky
def draw_sky_gradient(steps):
    r, g, b = 0, 128, 255
    step_height = 600 / steps

    for i in range(steps):
        r += int((135 - 0) / steps)
        g += int((206 - 128) / steps)
        b += int((250 - 255) / steps)

        t.penup()
        t.goto(-300, 300 - i * step_height)
        t.setheading(0)

        t.fillcolor(r, g, b)
        t.begin_fill()

        for _ in range(2):
            t.forward(600)
            t.right(90)
            t.forward(step_height)
            t.right(90)

        t.end_fill()


# drawing a white clouds
def draw_circle(x, y, radius, color):
    """지정 위치(x, y)에 색상과 반지름을 가진 원을 그림"""
    t.penup()
    t.goto(x, y - radius)  
    t.pendown()
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_cloud(x, y, scale=1.0):
    
    circles = [
        (0, 0, 30),
        (25, 10, 25),
        (-25, 10, 25),
        (50, 0, 20),
        (-50, 0, 20),
    ]
    for cx, cy, r in circles:
        draw_circle(x + cx * scale, y + cy * scale, r * scale, "white")
    


draw_sky_gradient(20)

draw_cloud(-120, 170, 1.2)
draw_cloud(180, 140, 1.0)
draw_cloud(10, -30, 0.8)
draw_cloud(120, -150, 0.9)
draw_cloud(-180, -150, 0.9)

screen.mainloop()



screen.mainloop()
