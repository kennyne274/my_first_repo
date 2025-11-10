import turtle  # Import the turtle graphics module

turtle.bgcolor("wheat")  # Set the background color to wheat
t = turtle.Turtle()  # Create a turtle object
t.pensize(3)  # Set the pen thickness to 3
t.speed(9)  # Set the turtle's drawing speed (9 is fast)

# Define a list of colors to use
colors = ["crimson", "orange", "teal", "green", "navy", "purple", "skyblue"]

t.penup()  # Lift the pen to move without drawing
t.goto(0, -150)  # Move the turtle to the starting position
t.pendown()  # Put the pen down to start drawing

# Draw 30 concentric circles
for i in range(30):
    t.color(colors[i % 7])  # Cycle through the color list
    t.circle(i * 7 + 5)  # Draw a circle with increasing radius

turtle.done()  # Finish the turtle graphics and keep the window open
