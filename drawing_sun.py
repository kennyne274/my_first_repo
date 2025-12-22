#"This code creates a graphic that draws a flame-like effect resembling the sun on a black background.

import turtle
# Set up the screen
scr = turtle.Screen()
scr.setup(800, 700) 
scr.bgcolor("black")  
scr.title("The Sun") 
# Create and configure the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()  
#  Define a list of colors for the sun rays/effects
colors = ["orange", "red", "yellow", "white", "coral"]  
# Main drawing loop - repeat 180 times to create a full effect
for i in range(180):
    t.goto(0,0) # Return to the center of the screen
    t.color(colors[i % 5]) # Cycle through the 5 colors (i % 5 gives 0~4 repeatedly)
    t.forward(120)
    t.left(3)
    t.circle(50)
    t.forward(180)
    t.right(180)
# Keep the window open until closed by the user
turtle.done()
