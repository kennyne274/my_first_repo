import turtle as t

# 꽃잎 한장 그리는 함수
def draw_petal():
    for i in range(2):
        t.circle(160, 80)
        t.left(100)

# 꽃을 그리는 함수
def draw_flower(n, color):
    t.color(color) # 꽃잎 색상 지정 
    for _ in range(n): # 꽃잎 갯수
        t.begin_fill()
        draw_petal() #함수 안에 함수 호출로 벚꽃 완성
        t.left(360/n) 
        t.end_fill()

# 꽃술 그리기
def flower_b(color, size):
    t.penup()
    t.goto(0, -size) # 중심으로 이동
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)   
    t.end_fill()


t.bgcolor("ivory") # 배경색 설정
t.title("My Art")
t.speed(0)

# 함수를 이용하여 꽃 그리기
draw_flower(6, "pink") 
flower_b("yellow", 40)


t.hideturtle() # 터틀 숨기기
t.exitonclick() # 클릭으로 종료
