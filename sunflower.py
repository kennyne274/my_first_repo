import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(420, 340)
screen.bgcolor("black")

t.speed(0)
colors =["orange", "white"]
t.width(1)

angle = 137.5

for i in range(400):
    t.pencolor(colors[i%2])
    t.forward(i * 0.6)
    t.right(angle)

t.hideturtle()
screen.mainloop()
