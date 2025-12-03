# Beautiful turtle art that draws colorful small hearts around a large central heart
import turtle as t

# Screen settings (background color, speed, pen size, hide cursor)
t.bgcolor("ivory")
t.speed(2)
t.pensize(6)
t.hideturtle()

# Function to draw a heart (position, size, border color, fill color)
def draw_heart(x, y, size=180, border_color="red", fill_color="hotpink"):
   
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.color(border_color)
    t.fillcolor(fill_color)
    t.begin_fill()         
    
    # Drawing the heart shape
    t.left(45)
    t.forward(size)
    t.circle(size/2, 180)
    t.right(90)
    t.circle(size/2, 180)
    t.forward(size)
    
    t.end_fill()
    t.setheading(0)  

# Calling the function to draw hearts of different colors and sizes
draw_heart(0, -150)                    
draw_heart(-180, 80, size=60, fill_color="gold")    
draw_heart(220, -160, size=60, border_color="navy", fill_color="skyblue")   
draw_heart(200, 120, size=60, border_color="teal", fill_color="cyan") 
draw_heart(-200, -160, size=60, border_color="tomato", fill_color="orange") 
draw_heart(0, 180, size=60, border_color="green", fill_color="lightgreen")
draw_heart(0,-50, size=60, border_color="red", fill_color="deeppink")

# End
t.done()