import turtle as t

t.bgcolor("black")
t.speed(0)

colors = ["red", "yellow", "blue", "teal", "cyan", "magenta"]

for i in range(200):
    t.color(colors[i % len(colors)])   
    t.forward(i * 2)                  
    t.right(144)                  
    t.pensize(2)                       




t.hideturtle()
t.done()
