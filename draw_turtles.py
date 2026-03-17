import turtle
import random
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("cornsilk")
screen.title("My Turtle Art")

h = 0  # Start hue value from red

# Create 20 turtles with different colors, positions, orientations, and sizes
for j in range(20):
    t = turtle.Turtle()
    
    # Convert HSV to RGB for rainbow-like color distribution
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.065                  # Increment hue (~15 colors across 20 turtles)
    
    t.color(c)
    t.shape("turtle")
    t.penup()
    
    # Random starting position within screen bounds
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    t.goto(x, y)
    
    # Random heading (direction) between 0 and 360 degrees
    t.setheading(random.randint(0, 360))
    
    # Random size scaling (0.5x to 4.5x)
    size = random.uniform(0.5, 4.5)
    t.shapesize(stretch_wid=size, stretch_len=size)

# Keep the window open until clicked
turtle.done()
