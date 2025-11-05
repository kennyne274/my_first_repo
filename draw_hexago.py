import turtle
import random

# 터틀 설정
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.pensize(1)

# RGB 모드로 전환 (0~255 값 사용 가능)
turtle.colormode(255)

# 육각형을 그리는 함수
def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

# 회전하며 무작위 색으로 육각형을 그리기
for i in range(100):
    # 무작위 RGB 색상 생성
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    t.color(r, g, b)
    
    # 육각형 그리기
    draw_hexagon(100)
    
    # 회전 각도
    t.right(3.6)

# 터틀 숨기기
t.hideturtle()
turtle.done()