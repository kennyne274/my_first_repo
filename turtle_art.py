import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("cornsilk")
screen.title("My turtle art")

colors = ["red", "orange", "yellow", "green", "blue", "gold", "coral", "purple", "pink", "cyan", "magenta", "teal", "skyblue", "teal", "navy"]

# 터틀 15마리 생성
turtles = []

for i in range(15):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    
    # 랜덤 위치 지정
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    t.goto(x, y)
    
    # 랜덤 방향 설정
    t.setheading(random.randint(0, 360))
    
    # 랜덤 크기 설정 (가로, 세로 크기)
    size = random.uniform(0.5, 4.5)  # 0.5배 ~ 3.5배 크기
    t.shapesize(stretch_wid=size, stretch_len=size)
    
    turtles.append(t)

# 화면 유지
turtle.done()
