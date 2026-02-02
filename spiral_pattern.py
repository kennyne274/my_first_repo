import turtle

t = turtle.Turtle()
t.pensize(2)
colors = ["crimson","orange","teal","green","navy","purple","skyblue"]

t.speed(0)
t.hideturtle()
for i in range(200): 
    t.color(colors[i % 7])
    t.forward(i*2+3)

    t.left(119) 

turtle.exitonclick()
