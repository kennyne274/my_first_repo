import turtle
import colorsys

t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(1)
t.shape("arrow")
t.pensize(1)

# Hue starts at 0 (red)
h = 0

# Draw 30 radial lines (360 / 12 = 30)
for angle in range(0, 360, 12): 
    # Increment hue for next line (0.032 × 30 ≈ 0.96 → almost one full rainbow cycle)
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h += 0.032
    t.setheading(angle)
    t.forward(200)
    t.backward(200)

t.hideturtle()
turtle.done()
