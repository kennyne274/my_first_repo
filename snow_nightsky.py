import turtle
import random


# You will have beautiful white snowflakes adorning the dark night sky.

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("white")


def koch_curve(length, depth):
  """
    Recursively draw a single segment of the Koch snowflake curve.
    
    Args:
        length (float): length of the current segment
        depth (int): recursion depth (0 = straight line)
    """
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(length / 3, depth - 1)
        t.left(60)
        koch_curve(length / 3, depth - 1)
        t.right(120)
        koch_curve(length / 3, depth - 1)
        t.left(60)
        koch_curve(length / 3, depth - 1)


#Draw one complete filled snowflake using three Koch curves.
def draw_snowflake(size, depth):
    t.begin_fill()
    for _ in range(3):
        koch_curve(size, depth)
        t.right(120)
    t.end_fill()

#Create multiple random snowflakes across the screen.
def random_snowflakes(count):
    # # Get current window dimensions (in pixels)
    width, height = screen.window_width(), screen.window_height()

    for i in range(count):
        x = random.randint(-width // 2 , width // 2)
        y = random.randint(-height // 2, height // 2)

        size = random.randint(20, 40) 
        depth = 3

        t.penup()
        t.goto(x, y)
        t.setheading(random.randint(0, 360))
        t.pendown()

        t.fillcolor("white")
        draw_snowflake(size, depth)


# ──────────────── Main Execution ────────────────
random_snowflakes(25)

screen.mainloop()

