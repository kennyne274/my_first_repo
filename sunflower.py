import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(420, 340)
screen.bgcolor("black")

t.speed(0)

def sunflower(a, b):
    colors =[a, b]
    t.width(1)

    angle = 137.5

    for i in range(300):
        t.pencolor(colors[i%2])
        t.forward(i * 0.6)
        t.right(angle)
   
sunflower("orange", "white")

t.hideturtle()
screen.mainloop()
