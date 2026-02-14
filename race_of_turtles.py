# turtle race
import turtle
import random


screen = turtle.Screen()
screen.title("🐢 Turtle Race Game")
screen.setup(width=800, height=600)
screen.bgcolor("ivory")

# Draw the finish line
finish_line = 330
line_drawer = turtle.Turtle()
line_drawer.hideturtle()
line_drawer.pensize(5)
line_drawer.pencolor("teal")
line_drawer.penup()
line_drawer.goto(finish_line, -280)
line_drawer.pendown()
line_drawer.left(90)
line_drawer.forward(560)

# List of turtle colors
colors = ["red", "blue", "green", "orange", "pink", "purple"]


turtles = []

# Create the turtles
for i in range(6):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-350, -250 + i * 100)
    turtles.append(t)

# race
winner = None

while True:
    for t in turtles:
        distance = random.randint(1, 10)
        t.forward(distance)

        # Check if any turtle has crossed the finish line
        if t.xcor() >= finish_line:
            winner = t.pencolor()
    
    if winner:
        break


# Display the winner message
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 150)
message.color(winner)
message.write(f"{winner} Turtle Wins!", align="center", font=("Arial", 35, "bold"))

screen.exitonclick()
