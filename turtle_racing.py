import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Run Game")
screen.bgcolor("ivory")

# Draw the finish line
finish_line = turtle.Turtle()
finish_line.pensize(7)
finish_line.pencolor("teal")
finish_line.penup()
finish_line.goto(250, 300)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(600)
finish_line.hideturtle()

# First turtle (red)
t1 = turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.goto(-200, 50)

# Second turtle (blue)
t2 = turtle.Turtle()
t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.goto(-200, -50)

# Third turtle (orange)
t3 = turtle.Turtle()
t3.color("orange")
t3.shape("turtle")
t3.penup()
t3.goto(-200, 150)

# Fourth turtle (purple)
t4 = turtle.Turtle()
t4.color("purple")
t4.shape("turtle")
t4.penup()
t4.goto(-200, -150)

# Fifth turtle (pink)
t5 = turtle.Turtle()
t5.color("hotpink")
t5.shape("turtle")
t5.penup()
t5.goto(-200, 250)

# Sixth turtle (green)
t6 = turtle.Turtle()
t6.color("green")
t6.shape("turtle")
t6.penup()
t6.goto(-200, -250)

# Start the race
while True:
    # Each turtle moves forward randomly
    t1.forward(random.randint(1, 10))
    t2.forward(random.randint(1, 10))
    t3.forward(random.randint(1, 10))
    t4.forward(random.randint(1, 10))
    t5.forward(random.randint(1, 10))
    t6.forward(random.randint(1, 10))

    # Check if any turtle reached the finish line
    if t1.xcor() >= 250:
        t1.penup()
        t1.goto(0, 0)
        t1.write("Red turtle wins!", align="center", font=("Arial", 30, "bold"))
        break
    elif t2.xcor() >= 250:
        t2.penup()
        t2.goto(0, 0)
        t2.write("Blue turtle wins!", align="center", font=("Arial", 30, "bold"))
        break
    elif t3.xcor() >= 250:
        t3.penup()
        t3.goto(0, 0)
        t3.write("Orange turtle wins!", align="center", font=("Arial", 30, "bold"))
        break
    elif t4.xcor() >= 250:
        t4.penup()
        t4.goto(0, 0)
        t4.write("Purple turtle wins!", align="center", font=("Arial", 30, "bold"))
        break
    elif t5.xcor() >= 250:
        t5.penup()
        t5.goto(0, 0)
        t5.write("Pink turtle wins!", align="center", font=("Arial", 30, "bold"))
        break
    elif t6.xcor() >= 250:
        t6.penup()
        t6.goto(0, 0)
        t6.write("Green turtle wins!", align="center", font=("Arial", 30, "bold"))
        break

screen.mainloop()
