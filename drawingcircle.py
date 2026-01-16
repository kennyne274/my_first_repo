import turtle  # Import the turtle graphics module

turtle.bgcolor("wheat")  # Set the background color to wheat
t = turtle.Turtle() 
t.pensize(3)
t.speed(9)  

# Define a list of colors to use
colors = ["crimson", "orange", "teal", "green", "navy", "purple", "skyblue"]

t.penup() 
t.goto(0, -150)  
t.pendown()  

# Draw 30 concentric circles
for i in range(30):
    t.color(colors[i % 7]) 
    t.circle(i * 7 + 5) 

turtle.done()  
