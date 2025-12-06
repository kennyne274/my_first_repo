import turtle as t

# ────────────────────────
# 1. Ask the user
# ────────────────────────
name = t.textinput("Create a Fractal Snowflake", "What's your name? (If canceled, I'll call you 'Friend')")
if not name:  # If canceled or empty
    name = "Friend"

size = t.numinput("Snowflake Size", "How big should the snowflake be? (100~500)", default=200, minval=100, maxval=500)
if not size:
    size = 200

depth = t.numinput("Fractal Depth", "How complex should it be? (Recommended 3~6)", default=4, minval=2, maxval=6)
if not depth:
    depth = 4

line_color = t.textinput("Choose Color", "What color should the snowflake be? (white, cyan, gold, pink, etc.)")
if not line_color:
    line_color = "white"

# ────────────────────────
# 2. Basic Settings
# ────────────────────────
t.speed(0)
t.hideturtle()
t.bgcolor("black")
t.color(line_color, "white")
t.pensize(2)

# ────────────────────────
# 3. Koch Snowflake Functions
# ────────────────────────
def koch_curve(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(length/3, depth-1)
        t.left(60)
        koch_curve(length/3, depth-1)
        t.right(120)
        koch_curve(length/3, depth-1)
        t.left(60)
        koch_curve(length/3, depth-1)

def draw_snowflake(size, depth):
    t.begin_fill()
    for _ in range(3):
        koch_curve(size, depth)
        t.right(120)
    t.end_fill()

# ────────────────────────
# 4. Draw Snowflake + Write Messages
# ────────────────────────
t.penup()
t.goto(0, size/2 + 50)
t.pendown()
t.write(f"❄I love you, {name}❄", align="center", font=("Arial", 30, "bold"))

t.penup()
t.goto(-size/2, 50)
t.pendown()
draw_snowflake(size, int(depth))

t.penup()
t.goto(0, -size/2 - 100)
t.write("Merry Christmas & Happy New Year!", align="center", font=("Arial", 20, "italic"))
t.done()