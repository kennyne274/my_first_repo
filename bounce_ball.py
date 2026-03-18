from tkinter import *
import random

def move():
    global x_speed, y_speed
    ball_coor = canvas.coords(ball)
    if ball_coor[0] <= 0 or ball_coor[2] >= WIDTH:
        x_speed = -x_speed
    if ball_coor[1] <= 0 or ball_coor[3] >= HEIGHT:
        y_speed = -y_speed
    canvas.move(ball, x_speed, y_speed)

    # Change color when the ball hits the wall
    if ball_coor[0] <= 0 or ball_coor[2] >= WIDTH or \
        ball_coor[1] <= 0 or ball_coor[3] >= HEIGHT:
     
        canvas.itemconfig(ball, fill=random.choice([
            "lightgreen", "hotpink", "violet", "cyan", "lime", "yellow", "orange"
        ]))
    root.after(30, move)
    

root = Tk()

root.title("Bouncing the ball")
WIDTH = 500
HEIGHT = 360

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

ball= canvas.create_oval(10,10,80,80, fill="#491CB3")

x_speed = random.randint(3, 10)
y_speed = random.randint(3, 10)

move()
root.mainloop()
