import turtle


x = -200
y = -200


pieces = {
    (0,0): "♜",(1,0): "♞",(2,0): "♝",(3,0): "♛",
    (4,0): "♚",(5,0): "♝",(6,0): "♞",(7,0): "♜",

    (0,1): "♟",(1,1): "♟",(2,1): "♟",(3,1): "♟",
    (4,1): "♟",(5,1): "♟",(6,1): "♟",(7,1): "♟",

    (0,6): "♙",(1,6): "♙",(2,6): "♙",(3,6): "♙",
    (4,6): "♙",(5,6): "♙",(6,6): "♙",(7,6): "♙",

    (0,7): "♖",(1,7): "♘",(2,7): "♗",(3,7): "♕",
    (4,7): "♔",(5,7): "♗",(6,7): "♘",(7,7): "♖",
}


def draw():
    for _ in range(4):
        t.fd(50)
        t.left(90)
    t.fd(50)

# drawing chess board
def draw_board():
    for i in range(8):
        t.up()
        t.goto(x, y+50*i)
        t.down()
        for j in range(8):
            if (i+j)%2 == 0:
                col = 'black'
            else:
                col = 'white'

            t.fillcolor(col)
            t.begin_fill()
            draw()
            t.end_fill()


#drawing chess pieces
def draw_pieces():
    for (x1, y2), symbol in pieces.items():

        screen_x = x + x1 * 50 + 50/2
        screen_y = y + y2 * 50 + (50/2) - 25

        p.goto(screen_x, screen_y)
        p.write(symbol, align="center",font=("Arial", 30, "normal"))


# basic set up
sc = turtle.Screen()
sc.title("chess board")
sc.setup(600, 600)

p = turtle.Turtle()
p.speed(0)
p.hideturtle()
p.penup()

t = turtle.Turtle()
t.speed(100)
t.pensize(2)

t.up()
t.goto(x, y)
t.down()
t.ht()
draw_board()
draw_pieces()

turtle.done()
