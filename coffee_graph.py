import turtle as t

def drawBar(height, color):
    t.fillcolor(color)
    t.pencolor("black")
    
    t.begin_fill()
    t.left(90)
    t.fd(height)
    t.write(str(height), font=('Arial', 14, 'bold'))
    t.right(90)
    t.fd(40)
    t.right(90)
    t.fd(height)
    t.left(90)
    t.end_fill()

data = [120, 56, 320, 220, 156, 103, 248, 32, 56]

colors = ["red", "yellow",  "orange", "hotpink", "green", "blue", "purple", "navy"]


t.bgcolor("ivory")
t.speed(0)
t.pensize(3)
t.penup()
t.goto(-180, -120)   
t.pendown()

for i, height in enumerate(data):
    color = colors[i % len(colors)]
    drawBar(height, color)

t.penup()


t.goto(0, 220)
t.pencolor("brown")
t.write("Average Daily Coffee Sales by Shop", align="center", font=("Arial", 22, "bold"))

# X
t.goto(0, -180)
t.pencolor("teal")
t.write("Coffee Shop Branches", align="center", font=("Arial", 16, "bold"))

# Y
t.goto(-180, -120)
t.pendown()
t.pencolor("black")
t.setheading(0)
t.forward(40*len(data))

t.hideturtle()
t.done()
