import turtle
import colorsys  

# -------------------------------
screen = turtle.Screen()
screen.setup(700, 700)           
screen.bgcolor("#0a0020")      
screen.tracer(0)                 

t = turtle.Turtle()
t.speed(0)
t.setheading(75)
t.penup()
t.goto(0, 0)
t.pendown()

# drawing a sunflower
# -------------------------------
def sunflower():
    angle = 137.50776405003785   
    base_width = 1.1
    max_width = 2.1

    for i in range(450):        
       
        width = base_width + (i / 450) * (max_width - base_width)
        t.width(width)

       
        hue = 0.08 + (i * 0.0009) % 0.12  
        saturation = 0.95 - (i / 1200)    
        value = 0.98                    

        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        t.pencolor(r, g, b)

        
        step = i * 0.78 + 3         
        t.forward(step)

    
        t.right(angle)

        
        if i % 40 == 0:
            screen.update()

# -------------------------------
sunflower()

# drawing a stem
t.setheading(280)
t.pencolor("teal")

for x in range(1,30):
    t.pensize(34 - x )
    t.forward(x / 2)
    
# drawing a leaf
t.setheading(50)
t.color("green")
for x in range(1,50):
    t.pensize(50 - x )
    t.forward(x / 5)
    
t.hideturtle()
screen.update()
screen.mainloop()
