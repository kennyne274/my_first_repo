import turtle as t

# 카카오 라이언 얼굴 그리기

# 눈과 코 그리기
def draw_eyes(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(20, "black")

# 눈썹 그리기
def draw_eyebrows(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(60)

# 배경 설정
t.bgcolor("ivory")
t.title("Face of Lion")
t.speed(9) # 그리기 속도
t.pensize(7) # 펜 굵기
t.color("black", "#f0a53a") # 그림을 그릴 선색과 채우기 색 지정

# 왼쪽 귀
t.penup()           # 펜 들기
t.goto(-110, 150)    # 좌표로 이동
t.pendown()         # 펜 다운
t.begin_fill()      
t.setheading(120)   # 터틀(화살표) 이동방향 120도 바꾸기
t.circle(50, 220)   # 원은 220도만 그린다.
t.end_fill()        

# 오른쪽 귀
t.penup()           # 펜 들기
t.goto(110, 150)     # 좌표로 이동
t.pendown()         # 펜 다운
t.begin_fill()      
t.setheading(60)    # 터틀(화살표) 이동방향 
t.circle(-50, 220)  # 원은 220도만 그린다. 
t.end_fill()        


# 얼굴 그리기
t.penup()
t.setheading(0)
t.goto(0, -200)
t.pendown()
t.fillcolor("#f0a53a") # 라이언 피부색
t.begin_fill()
t.circle(190)
t.end_fill()

# 함수 호출하여 눈 그리기
draw_eyes(-80,20)
draw_eyes(80,20)

#함수 호출하여 눈썹 그리기
t.pensize(10) # 눈썹은 가장 굵게
draw_eyebrows(50,50)
draw_eyebrows(-110,50)

# 라이언 코와 입 그리기

# 라이언 코 그리기
t.penup()
t.goto(0, -40)
t.pendown()

# 라이언 입 그리기
t.setheading(140)
t.fillcolor("white")
t.begin_fill()
t.circle(35,270)
t.setheading(310)
t.circle(35,270)
t.end_fill()

t.penup()
t.goto(5, -40)
t.pendown()
t.dot(25, "black")

t.hideturtle() # 커서 숨기기

t.done()