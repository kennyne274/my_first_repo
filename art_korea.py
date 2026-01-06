import turtle as t


def draw_art(turn, steps):

    colors =["red","yellow","blue"]
    t.bgcolor("black")
    t.speed(0)
    t.pensize(1)
    t.hideturtle()
    i = 0
    while True:
        t.color((colors[i%len(colors)]))
        t.forward(i)
        t.lt(turn)
        i += 1
        if i ==steps:
            break

if __name__=="__main__":
    draw_art(118, 1000)

t.done()
