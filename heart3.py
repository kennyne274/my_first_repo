
import turtle as t

# drawing a red heart
def draw_heart():
    t.fillcolor("red")
    t.begin_fill()
    t.left(45)
    t.forward(180)
    t.circle(90, 180)
    t.right(90)
    t.circle(90, 180)
    t.forward(180)
    t.end_fill()
    t.setheading(0)

# writing a message
def write_love():
    t.penup()
    t.goto(0,30)
    t.color("white")
    t.write("I love you", align="center", font=('Comic Sans MS', 30, 'italic'))
       
# drawing a lovely heart
def main():
    t.speed(1)
    t.bgcolor("black")
    t.pencolor("red")
    t.penup()
    t.goto(0, -90)
    t.pendown()
    draw_heart()
    write_love()
    t.hideturtle()
    t.done()

# Run the main function
if __name__ == "__main__":
    main()