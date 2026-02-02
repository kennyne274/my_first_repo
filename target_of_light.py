import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.hideturtle()
    

for angle in range(0, 360, 12):    
    t.setheading(angle)
    
    for dist in range(0, 220, 18):
        
        hue = (angle / 360 + dist / 800) % 1.0
        brightness = 0.3 + (dist / 220) * 0.7     
        saturation = 0.8 + (dist / 220) * 0.2     
        
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, brightness)
        t.pencolor(r, g, b)
        
        t.forward(dist)

        t.backward(dist)

turtle.done()
