import turtle as t
import random

# tree
def draw_branch(length, angle, level):
    if level == 0:
        return 
   
    t.pensize(level * 1.5)
    if level > 4:
        t.pencolor("brown")     
    elif level > 2:
        t.pencolor("sandybrown")
    else:
        t.pencolor("green") 
    
    t.forward(length)   
 
    t.right(angle)   
    draw_branch(length * 0.7, angle, level - 1)
  
    t.left(angle * 2)
    draw_branch(length * 0.7, angle, level - 1)
    
    t.right(angle)
    t.backward(length)

t.bgcolor("lightskyblue")  
t.tracer(2)       
t.penup()
t.goto(0, -250)
t.pendown()
t.left(90)         

draw_branch(140, 30, 11)   

# field
t.penup()
t.setheading(0)
t.goto(-400, -280)
t.pendown()
t.color("sienna")
t.pensize(100)
t.forward(800)

t.color("darkgreen")
t.pensize(10)

for x in range(-380, 381, 20):
    t.penup()
    t.goto(x, -230)
    t.pendown()
    t.setheading(random.randint(70, 110))
    t.forward(random.randint(20, 45))

# snow
for i in range(100):
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    size = random.uniform(3, 8)
    t.up()
    t.goto(x, y)
    t.dot(size, "white")

t.done()
