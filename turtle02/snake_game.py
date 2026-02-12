from turtle import*
import time
import random

"""A game where the snake eats food to increase the score. 
The more food it eats, the higher the score and the longer the snake's body becomes.
The game ends when the snake collides with its own body."""

# Direction key input functions

def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

# Generate random coordinates
def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y

# Update score
def score_update():
    global score
    score += 1
    score_count.clear()
    score_count.write(f"Score : {score}", font = ("Arial", 15, "bold"))

# Create snake body segment
def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orange")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

def game_over():
    game_over_text = Turtle()
    game_over_text.hideturtle()
    game_over_text.penup()
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER!", align="center", font=("Arial", 30, "bold"))

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("olive")
screen.tracer(0)

start_pos = [(0,0), (-20,0), (-40,0)]
snakes = []

score = 0

for pos in start_pos:
    create_snake(pos)

# Food
food = Turtle()
food.shape("circle")
food.color("red")
food.up()
food.speed(0)
food.goto(rand_pos())

# Score display
score_count = Turtle()
score_count.ht()
score_count.up()
score_count.goto(-270, 250)
score_count.write(f"SCORE : {score}", font = ("Arial", 15, "bold"))

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left,"Left")
screen.onkeypress(right, "Right")

# Game loop section
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(20)

    if snakes[0].distance(food) < 15:
        score_update()
        food.goto(rand_pos())
        create_snake(snakes[-1].pos())

    
    head_x = snakes[0].xcor()
    head_y = snakes[0].ycor()
    
    # X-axis: left end → right end, right end → left end
    if head_x > 290:
        snakes[0].setx(-290)
    elif head_x < -290:
        snakes[0].setx(290)
    
    # Y-axis: top end → bottom end, bottom end → top end
    if head_y > 290:
        snakes[0].sety(-290)
    elif head_y < -290:
        snakes[0].sety(290)

    # If it collides with its own body, game over 
    for body in snakes[1:]:
        if snakes[0].distance(body) < 10:
            game_on = False
            game_over()
            break


screen.exitonclick()
