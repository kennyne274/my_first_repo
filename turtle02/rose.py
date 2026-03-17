import colorsys
import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.tracer(2)

turtle.hideturtle()
for i in range(1000):
    color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
    turtle.color(color)
    turtle.forward(i*0.5)
    turtle.right(98) 

turtle.exitonclick()
