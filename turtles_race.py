import turtle as t
import winsound
import time
import random

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("ivory")

colors = ["hotpink", "white", "red", "green", "yellow", "purple", "blue"]
start_ycor =[150, 90, 30, -30, -90, -150, -210]
game_over = False
turtles =[]

t.up()
t.ht()

# Countdown before race
t.goto(0, 0)
t.color("red")
for count in ["3", "2", "1", "GO!"]:
    t.clear()
    t.write(count, align="center", font=("Arial", 120, "bold"))
    time.sleep(1)

# title
t.goto(0, 240)
t.color("teal")
t.write("Turtle Race", align= "center", font=("Arial", 30, "bold"))
t.speed(0)

# Draw race track
t.goto(-400, 170)
t.down()
t.color("#0CC7CE")
t.begin_fill()
for i in range(2):
    t.fd(800)
    t.right(90)
    t.fd(400)
    t.right(90)
t.end_fill()

# Draw finish line
t.color("white")
t.up()
t.goto(330, 200)
t.down()
t.goto(330, -250)

# Draw starting lines for each lane
for i in range(6):
    t.up()
    t.goto(-350, start_ycor[i] - 30)
    t.color("white")
    t.down()
    t.goto(350, start_ycor[i] - 30)


# Create 7 turtles
for i in range(7):
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(-350, start_ycor[i])
    new_turtle.write(i+1) 
    new_turtle.goto(-330, start_ycor[i])
    turtles.append(new_turtle)

# Get user's bet
user_choice = int(t.textinput("Turtle Race", "Which turtle will you bet on? (1-7)"))

t.up()
t.goto(0, -290)
t.color("teal")
t.write(f"You bet on turtle #{user_choice}", align= "center", font=("Arial", 18, "bold"))


# sound race start
winsound.Beep(523, 300)
time.sleep(0.3)

# game loop
while not game_over:
    for i in turtles:
        rand_speed = random.randint(1, 10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            game_over = True
            
# Find winner
max_xcor = 0
winner = 0
for i in range(len(turtles)):
    if turtles[i].xcor() > max_xcor:
        max_xcor = turtles[i].xcor()
        winner = i + 1

# show result
t.goto(0, 0)
t.color("red")
if user_choice == winner:
    t.write(f"You've won!!", align= "center", font=("Arial", 20, "bold"))
else:
    t.write("you lost!! -$100.", align= "center", font=("Arial", 20, "bold"))

t.done()
