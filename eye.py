import turtle

# Create the turtle screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

screen.setup(720, 520)
screen.bgcolor('black')

# Set up the color set 
colors = ['red', 'green', 'blue', 'yellow', 'purple']

t.pensize(0)
t.speed(0)
t.penup()
t.setpos(0, 0)
t.pendown()

# Draw the shape using different colors
for i in range(90):
    for i in range(5):
        t.pencolor(colors[i])
        t.forward(200)
        t.right(144)
    t.right(4)

# hide the turtle
t.ht()
screen.mainloop()
