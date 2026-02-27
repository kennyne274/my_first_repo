import turtle
import random

# Click to make stars 
screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#0a0015")
screen.title("Click to make magical stars ")

turtle.tracer(0)

def draw_star(x, y, size=18, color="white"):
    """
    Draw a filled star at the given (x, y) position.
    
    Args:
        x (float): x-coordinate
        y (float): y-coordinate
        size (float): length of one arm of the star
        color (str): fill color of the star
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def on_click(x, y):
    """Called when the user clicks on the screen.
    Creates a star with random size and color at the click position.
    """
    size = random.uniform(12, 32)
    colors = ["#ffffff", "#fffacd", "#81f0f0", "#f0e68c", "#add8e6"]
    draw_star(x, y, size, random.choice(colors))
    screen.update()

# Bind mouse click event
screen.onclick(on_click)
# Create 3 initial stars at random positions
for _ in range(3):
    draw_star(random.randint(-420,420), random.randint(-320,320))

screen.update()
screen.mainloop()
