import pygame
import random
import sys

# 초기화
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")

# 색상
BLACK = (0, 0, 0)  # 배경
WHITE = (255, 255, 255)  # 공
COLORS = [
    (255, 0, 0),    # 빨강
    (0, 255, 0),    # 초록
    (0, 0, 255),    # 파랑
    (255, 255, 0),  # 노랑
    (255, 165, 0)   # 주황
]

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 20
paddle_speed = 10

# 공 설정
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 4
ball_dy = -4

# 벽돌 설정
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 20
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
        color = COLORS[row % len(COLORS)]  # 행마다 다른 색상
        bricks.append((brick, color))

# 점수 및 폰트
score = 0
font = pygame.font.SysFont('Arial', 24, bold=True)

# 사운드 로드
pygame.mixer.init()
try:
    block_sound = pygame.mixer.Sound('block.wav')  # 벽돌 부수기
    paddle_sound = pygame.mixer.Sound('paddle.wav')  # 패들 충돌
    gameover_sound = pygame.mixer.Sound('gameover.wav')  # 게임 오버
    pygame.mixer.music.load('bgm.mp3')  # 배경 음악
    pygame.mixer.music.set_volume(0.3)  # 배경 음악 볼륨
    pygame.mixer.music.play(-1)  # 무한 루프 재생
except FileNotFoundError:
    print("사운드 파일(block.wav, paddle.wav, gameover.wav, bgm.mp3)을 다운로드하세요.")
    block_sound = paddle_sound = gameover_sound = pygame.mixer.Sound(pygame.mixer.Sound(buffer=bytearray(1000)))

block_sound.set_volume(0.5)
paddle_sound.set_volume(0.5)
gameover_sound.set_volume(0.6)

# 게임 루프
clock = pygame.time.Clock()
running = True
game_over = False
game_won = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (game_over or game_won):
            if event.key == pygame.K_r:  # 재시작
                ball_x, ball_y = screen_width // 2, screen_height // 2
                ball_dx, ball_dy = 4, -4
                paddle_x = (screen_width - paddle_width) // 2
                bricks = []
                for row in range(brick_rows):
                    for col in range(brick_cols):
                        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
                        color = COLORS[row % len(COLORS)]
                        bricks.append((brick, color))
                score = 0
                game_over = False
                game_won = False
                pygame.mixer.music.play(-1)  # 재시작 시 배경 음악 재생

    if not game_over and not game_won:
        # 키 입력
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # 공 이동
        ball_x += ball_dx
        ball_y += ball_dy

        # 벽 충돌
        if ball_x <= 0 or ball_x >= screen_width - ball_radius * 2:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy
        if ball_y >= screen_height:
            game_over = True
            gameover_sound.play()
            pygame.mixer.music.stop()  # 게임 오버 시 배경 음악 정지

        # 패들 충돌
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)
        if ball_rect.colliderect(paddle_rect):
            ball_dy = -ball_dy
            paddle_sound.play()

        # 벽돌 충돌
        for brick, color in bricks[:]:
            if ball_rect.colliderect(brick):
                bricks.remove((brick, color))
                ball_dy = -ball_dy
                score += 10
                block_sound.play()
                break

        # 승리 조건
        if not bricks:
            game_won = True
            pygame.mixer.music.stop()  # 승리 시 배경 음악 정지

    # 화면 그리기
    screen.fill(BLACK)  # 검은색 배경

    # 패들 (청록색 그라디언트)
    paddle_surface = pygame.Surface((paddle_width, paddle_height))
    for x in range(paddle_width):
        color = (0, 100 + x, 255 - x // 2)
        pygame.draw.line(paddle_surface, color, (x, 0), (x, paddle_height))
    screen.blit(paddle_surface, (paddle_x, paddle_y))

    # 공 (하얀색, 반짝이는 원)
    ball_surface = pygame.Surface((ball_radius * 2, ball_radius * 2), pygame.SRCALPHA)
    for r in range(ball_radius, 0, -1):
        alpha = 255 - (r * 10)
        pygame.draw.circle(ball_surface, (255, 255, 255, alpha), (ball_radius, ball_radius), r)
    screen.blit(ball_surface, (ball_x, ball_y))

    # 벽돌 (알록달록, 부드러운 그라디언트 질감)
    for brick, base_color in bricks:
        brick_surface = pygame.Surface((brick.width, brick.height), pygame.SRCALPHA)
        for y in range(brick.height):
            for x in range(brick.width):
                # 중앙이 밝고 가장자리가 어두운 그라디언트
                distance = ((x - brick.width / 2) ** 2 + (y - brick.height / 2) ** 2) ** 0.5
                max_distance = (brick.width ** 2 + brick.height ** 2) ** 0.5 / 2
                intensity = max(0, 1 - distance / max_distance)
                r = int(base_color[0] * intensity)
                g = int(base_color[1] * intensity)
                b = int(base_color[2] * intensity)
                alpha = int(255 * intensity)
                brick_surface.set_at((x, y), (r, g, b, alpha))
        screen.blit(brick_surface, (brick.x, brick.y))
        # 흰색 테두리 유지
        pygame.draw.rect(screen, WHITE, brick, 1)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 게임 오버/승리 화면
    if game_over:
        over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(over_text, (screen_width // 2 - 150, screen_height // 2))
    elif game_won:
        win_text = font.render("You Won! Press R to Restart", True, (0, 255, 0))
        screen.blit(win_text, (screen_width // 2 - 130, screen_height // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()import turtle

# 스크린 설정
screen = turtle.Screen()
screen.setup(width=600, height=600)

# 터틀 설정
t = turtle.Turtle()
t.speed(0)  # 빠른 그리기를 위해 속도를 0으로 설정
t.penup()
t.goto(-300, 300)

# RGB 모드를 255로 설정
screen.colormode(255)

# 하늘 그라데이션 그리기 함수
def draw_sky_gradient(steps):
    # 초기 색상: 짙은 파란색
    r, g, b = 0, 128, 255

    step_height = 600 / steps  # 각 단계별 높이

    for i in range(steps):
        # 위로 갈수록 옅어지는 하늘색 만들기
        r += int((135 - 0) / steps)  # 135는 옅은 하늘색의 빨간색 값
        g += int((206 - 128) / steps)  # 206은 옅은 하늘색의 녹색 값
        b += int((250 - 255) / steps)  # 250은 옅은 하늘색의 파란색 값

        t.fillcolor(r, g, b)
        t.begin_fill()

        # 사각형 그리기 (외곽선을 그리지 않음)
        t.goto(-300, 300 - i * step_height)  # 시작 위치 설정
        t.setheading(0)  # 방향을 오른쪽으로 설정

        # 펜을 들어올려 외곽선이 그려지지 않도록 설정
        t.forward(600)
        t.right(90)
        t.forward(step_height)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(step_height)
        t.right(90)

        t.end_fill()

# 단계 수 설정 (20단계로 그라데이션)
draw_sky_gradient(20)

# 터틀 종료
t.hideturtle()
screen.mainloop()



try:
    # 파일 열기
    with open("log.txt", "r") as file:
        text = file.read()

    # 단어 수 세기
    words = text.split()

    # 글자 수 세기
    letters = sum(1 for i in text if i.isalpha())

    # 단어 빈도 계산
    target = input("찾고 싶은 단어를 입력하세요: ").lower()
    count = sum(1 for word in words if word.lower() == target)

    # 결과 출력
    print("파일 내용 분석")
    print("단어 갯수:", len(words))
    print("글자 수:", letters)
    print(f"'{target}' 등장 횟수:", count)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다!")
except Exception as e:
    print("오류 발생:", e)import turtle
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
from datetime import date

print("요일 확인 프로그램")
print("종료하려면 q를 입력하세요.")
while True:
    try:
        #사용자에게 날짜를 입력 받습니다.
        year1 = input("연도를 숫자로 입력하세요. 예) 2025 :")
        if year1 == "q":
            print("종료합니다")
            break
        year = int(year1)
        month1 = input("(월을 숫자만 입력하세요. 예) :")
        if month1 == "q":
            print("종료합니다.")
            break
        month = int(month1)
        day1 = input("날짜를 숫자만 입력하세요. 예) 23 :")
        if day1 == "q":
            print("종료합니다")
            break
        day = int(day1)

        #날짜 객체 생성
        d = date(year, month, day)
        #평일 주말 확인
        if d.weekday() >= 5:
            day_type = "주말"
        else:
            day_type = "평일"

        #요일 이름 출력
        day_name = d.strftime("%A")

        print(f"{d}는 {day_name}, {day_type}입니다")
        
    
    except ValueError as e:
        print("잘못 입력했습니다. 다시 입력하세요", e)import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("cornsilk")
screen.title("My turtle art")

# 색상 목록 
colors = ["red", "orange", "yellow", "green", "blue", "cyan", "pink", "purple","skyblue", "coral"]

# 터틀 15마리 생성
turtles = []

for i in range(15):
    selected_color = random.choice(colors) # 목록에서 색상을 랜덤으로 선택
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(selected_color)
    t.penup()
    
    # 랜덤 위치 지정
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    
    # 랜덤 방향 설정
    t.setheading(random.randint(0, 360))
    
    # 랜덤 크기 설정 (가로, 세로 크기)
    size = random.uniform(0.5, 3.5)  # 0.5배 ~ 3.5배 크기
    t.shapesize(stretch_wid=size, stretch_len=size)
    
    turtles.append(t)

# 화면 유지
turtle.done()from datetime import datetime

password = input("Enter password: ")
if not password:
    print("Empty input!")
elif len(password) >= 8:
    print("Secure!")
    with open("C:/python/log.txt", "a") as file:  # 절대 경로 지정
        file.write(f"{datetime.now()}: Secure password\n")
else:
    print("Weak!")
    with open("C:/python/log.txt", "a") as file:  # 절대 경로 지정
        file.write(f"{datetime.now()}: Weak password\n")import random
import turtle
# 화면 설정
colors = ["coral","orange","lightyellow","lime","palegreen","plum","purple","skyblue"]

screen = turtle.Screen()
screen.bgcolor(random.choice(colors))
screen.title("My turtle art")

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.color(random.choice(colors), random.choice(colors))
t.begin_fill()

for i in range(0,10):
    t.right(36)
    for i in range(0,8):
        t.forward(75)
        t.right(45)
t.end_fill()
turtle.done()



# 사용자 정의 함수로 숫자의 절대값 구하기

from datetime import datetime
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
try:
    num = float(input("숫자를 입력하시요 : "))
    result = my_abs(num)
    print(result)
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | ABS | input={num} | output={result}\n")
except ValueError as e:
    print("숫자만 입력하세요 : ")
    with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | ERROR| {e} \n")

import math
from datetime import datetime
try:
    n = int(input("Enter a number: "))
    if n < 2:
        print("No")
        with open("C:/python/prime.log", "a", encoding="UTF8") as f:
            f.write(f"{datetime.now()} | PRIME | n={n} | result=No\n")
        
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Yes")
            with open("C:/python/prime.log", "a", encoding="UTF8") as f:
                        f.write(f"{datetime.now()} | PRIME | n={n} | result=Yes\n")
        else:
            print("No")
            with open("C:/python/prime.log", "a", encoding="UTF8") as f:
                        f.write(f"{datetime.now()} | PRIME | n={n} | result=No\n")
except ValueError:
    print("Please enter a number!")
    with open("C:/python/prime.log", "a", encoding="UTF8") as f:
        f.write(f"{datetime.now()} | ERROR | Invalid input\n")




from datetime import datetime
try:
    text = input("이름을 입력하세요 : ")
    if len(text) >= 3:
        rev = text[2] + text[1] + text[0] #하드 코딩 인덱스
        rev = rev.lower()
    
        print("Hello, " + rev + "!")
        
        with open("greet.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | name | = {text} | greet | = Hello, {rev}!\n")
    else:
        print("세 글자 이상 입력하세요.")
        with open("greet.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | name | = {text} | error | = 세 글자 이상 입력하세요!\n")

except IndexError as e:
    print("세 글자 이상 입력!", e)
    
    with open("greet.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | ERROR | = {e} \n")
from datetime import datetime
while True:
    choice = input("Try again? (y/n): ").lower()
    if choice == 'n':
        print("Game over.")
        break
    try:
        num = int(input("숫자를 맞춰봐 : "))
        if num >= 6:
            print("Correct!")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}|CORRECT={num}|\n")
            break
        elif 4 <= num < 6:
            print("Good! Try again")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}|GOOD={num}|\n")
        else:
            print("Try again")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}|TRY AGAIN={num}|\n")
    except ValueError as e:
        print("Enter a number", e)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()}|ERROR={e}|\n")
# This password checker is safe and block the danger.
# Note: uses "decoy" for fake examples and keeps an "audit" trail in the log.
# Use shell to set flag on decoy hit.
# "Decoy" entries may be used for testing, but do not affect real blocking decisions.
# Critical alerts are flagged and recorded for further review.
# Beacon vs Rootkit: signals are visible, hidden threats are exposed.
# Payload and Tunneling: payload is the content, tunneling is the hidden path.
# Hackers exploit vulnerabilities in the system through backdoor.
# Warning: intrusion and obfuscation

from datetime import datetime

checked_count = 0  # Counter for checker emails
seen_emails = set()

while True:
    try:
        email = input("Enter an email: ").lower()
    except Exception as e:
        print((f"Input error : ",e))
        continue
    
    if email == "stop":
        print("Program ended.")
        print(f"Emails checked: {checked_count}")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Program ended| {email} |Emails checked={checked_count}\n")
        break

    checked_count += 1

    if email in seen_emails:
        print("Duplicate detected.")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Duplicate detected| {email} |Emails checked={checked_count}\n")
    else:
        seen_emails.add(email)


    if '@' not in email:
        print("Invalid format!")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Invalid format| {email} |Emails checked={checked_count}\n")
    elif email == "decoy@trap.com":
        print("Decoy triggered!")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Decoy triggered| {email} |Emails checked={checked_count}\n")
        # Fake beacon log
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Beacon: {email} active| Emails checked={checked_count}\n")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |OSINT: Port 80 open on target| {email} |Emails checked={checked_count}\n")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Scan: Target IP 192.168.1.1 open| {email} |Emails checked={checked_count}\n")
        

    elif len(email) < 5:
        # Optional short-length warning
        print("Too short!")
        
    elif len(email) >= 50:   
        print("Too long! Possible spoof!")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Possible spoof| {email} |Emails checked={checked_count}\n")

    elif "bank" in email or "login" in email:
        print("Danger!")

        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Danger| {email} |Emails checked={checked_count}\n")
    else:
        print("Safe.")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |Safe| {email} |Emails checked={checked_count}\n")# backdoor_alert 함수를 정의함
from datetime import datetime
def backdoor_alert(ip):
    if ip in ["192.168.1.1", "10.0.0.1"]:
        print("Backdoor detected! Pivot blocked!")
        with open("C:/python/logfile.txt", "a", encoding='utf-8') as f:
            f.write(f"{datetime.now()}|dangerous={ip}|\n")
    else:
        print("Clean.")
        with open("C:/python/logfile.txt", "a", encoding='utf-8') as f:
            f.write(f"{datetime.now()}|clean={ip}|\n")
while True:
    user_ip = input("Enter your ip address : ").strip()
    backdoor_alert(user_ip)
    if input("Continue? (y/n): ").lower() != 'y':
        breakimport turtle

t = turtle.Turtle()
t.pensize(3)
t.pencolor("green")

for i in range(3):
    t.forward(200)
    t.left(120)

turtle.done()
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
turtle.done()import turtle

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("wheat")  
screen.title("Various Shapes")

# 터틀 객체 생성
t = turtle.Turtle()
t.pensize(2)
t.speed(3)  # 그리기 속도

# 위치 이동 함수 (겹침 방지)
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 1. 원 (Circle)
move_to(-300, 0)
t.color("red","orange")
t.begin_fill()
t.circle(50)  # 반지름 50
t.end_fill()

# 2. 삼각형 (Triangle)
move_to(-200, 0)
t.color("red","plum")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# 3. 사각형 (Square)
move_to(-100, 0)
t.color("indigo","lime")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# 4. 직사각형 (Rectangle)
move_to(0, 0)
t.color("orange","tomato")
t.begin_fill()
for _ in range(2):
    t.forward(150)  # 가로
    t.left(90)
    t.forward(80)   # 세로
    t.left(90)
t.end_fill()

# 5. 오각형 (Pentagon)
move_to(100, 0)
t.color("navy","teal")
t.begin_fill()
for _ in range(5):
    t.forward(80)
    t.left(360 / 5)
t.end_fill()

# 6. 별 (Star)
move_to(200, 0)
t.color("yellow","greenyellow")
t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(144)  # 144도 회전 (별 모양)
t.end_fill()

# 7. 육각형 (Hexagon)
move_to(-300, -150)
t.color("black","hotpink")
t.begin_fill()
for _ in range(6):
    t.forward(70)
    t.left(360 / 6)
t.end_fill()

# 8. 중첩 다각형 (Nested Polygons)
move_to(-100, -150)
t.color("brown","lavender")
t.begin_fill()
for i in range(5):  # 5개 중첩
    t.circle(20 + i * 20, steps=6)  # 6각형, 크기 점진 증가
    t.left(360 / 5)  # 회전
t.end_fill()

# 클릭으로 종료
screen.exitonclick()import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle() 
t.pensize(3) # 도형과 텍스트만 보기 위해 숨김
t.speed(0)      # 빠른 그리기

# 색상 목록
colors = [
     "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid",
    "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray",
    "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
    "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite",
    "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold"
]

# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이 (원 반지름 30의 2배)
rect_height = 30  # 세로 길이 (원 반지름과 동일)
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(5):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        t.fillcolor(colors[color_idx])  # 색상 채우기
        t.begin_fill()
        for _ in range(2):  # 가로, 세로 반복
            t.forward(rect_width)  # 가로
            t.left(90)
            t.forward(rect_height)  # 세로
            t.left(90)
        t.end_fill()

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))

# 프로그램 종료
turtle.done()from datetime import datetime
import random
import turtle

# 컴퓨터가 1~7 사이의 숫자를 랜덤으로 생성
num = random.randint(1,7)
# 기회는 5회 주어집니다.
attempts = 5
while attempts > 0:
    try:
        guess = int(input("Enter a number : "))
        if num == guess:
            print("correct")
            # 성공시 터틀이 중첩된 다각형을 그립니다.
            # 화면 설정
            screen = turtle.Screen()
            screen.bgcolor("lightyellow")  # 배경색 추가
            screen.title("랜덤 도형 생성")
            t = turtle.Turtle()
            t.pensize(3)
            t.color("red","orange")
            t.begin_fill()
        
            for i in range(0,10):
                t.right(36)
                for i in range(0,3):
                    t.forward(200)
                    t.right(120)
            t.end_fill()
            turtle.done()
            break

        elif guess > num:
            print("Too high! Try again.")
            
        else:
            print("Too low! Try again.")
        attempts -= 1
    except ValueError as e:
        print("Only number", e)
        #로그는 연습용이니 무시하셔도 되요.
        with open("log.txt","a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} Error {e}\n")
if attempts == 0:
    print(f"Game over! 정답은 {num}였습니다.")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} Game over, answer was {num}\n")
# This password checker is safe and block the danger.

from datetime import datetime

while True:
    email = input("Enter an email: ").lower()
    if email == "stop":
        print("Program ended.")
        with open("C:/python/email_log.txt", "a", encoding="UTF8") as f:
            f.write(f"{datetime.now()} |Program ended| {email}\n")
        break
    elif len(email) >= 50:   #  이메일 길이 검사 추가
        print("Too long! Possible spoof!")
        with open("C:/python/email_log.txt", "a", encoding="UTF8") as f:
            f.write(f"{datetime.now()} |Possible spoof| {email}\n")
    elif "bank" in email or "login" in email:
        print("Danger!")
        with open("C:/python/email_log.txt", "a", encoding="UTF8") as f:
            f.write(f"{datetime.now()} |Danger| {email}\n")
    else:
        print("Safe.")
        with open("C:/python/email_log.txt", "a", encoding="UTF8") as f:
            f.write(f"{datetime.now()} |Safe| {email}\n")
import turtle
import random

# 터틀 설정
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(9)
t.pensize(2)

# RGB 모드로 전환 (0~255 값 사용 가능)
turtle.colormode(255)

# 회전하며 무작위 색으로 도형 그리기
for _ in range(100):
    # 무작위 RGB 색상 생성
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    t.color(r, g, b)
    # 정사각형 그리기
    for i in range(4):
        t.forward(150)
        t.right(90)

    
    # 회전 각도
    t.right(3.6)

# 터틀 숨기기
t.hideturtle()
turtle.exitonclick()#include <stdio.h>

int main() {
    printf("Hello\n");
    return 0;
}import turtle

t = turtle.Turtle()
t.pensize(2)
colors = ["crimson","orange","teal","green","navy","purple","skyblue"]

t.speed(0)
t.hideturtle()
for i in range(200): 
    t.color(colors[i % 7])
    t.forward(i*2+3)

    t.left(119) 

turtle.exitonclick()import turtle
scr = turtle.Screen()
scr.setup(800, 700)  # 화면 크기 설정
scr.bgcolor("wheat")  # 배경색
scr.title("My turtle Art")  # 제목
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(9)
t.hideturtle()  # 커서 숨김
t.penup()  # 펜 들어
t.goto(-175, 0)  # -175,0 좌표로 이동
t.pendown()  # 펜 내려
colors = ["orange", "red", "orangered", "salmon", "crimson", "coral", "darkorange"]  # 사용할 색상을 리스트에 담아줌
for i in range(36):
    t.color(colors[i % 7])
    t.forward(350)
    t.left(170)
turtle.done()import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(0)
t.hideturtle() # 터틀 숨기기

for i in range(100):
    t.color(i/100,i/100,0)
    for j in range(0,4):
        t.forward(150)
        t.right(90)
    t.right(3.6)
   
turtle.exitonclick()# 파일에 저정된 단어와 글자수 확인 프로그램
import sys
filename = input("Type a file name : ")
try:
    with open(filename,"r", encoding="utf-8") as file:
        text = file.read() # 파일 내용 읽기
except FileNotFoundError as e:
    print("파일을 발견할 수 없습니다", e)
    sys.exit() # 프로그램 종료
    
# 파일에서 단어 정리하기
words = text.split()

# 글자 수 확인(알파벳만)
letters = 0
for i in text:
    if i.isalpha():
        letters += 1

# 단어 빈도 검사

target = input("Type a word : ").lower()
count = 0
for word in words:
    if word.lower() == target:
        count += 1


print("파일 내용 확인")
print("단어 수", len(words))
print("글자수", letters)
print(f"{target}, 등장 횟수 {count}")
print("num1")

​
import random
import turtle

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("lightyellow")  # 배경색 추가
screen.title("랜덤 도형 생성")

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.color(random.choice(["red", "blue", "green", "purple"]), random.choice(["yellow", "lightblue", "pink", "black"]))
t.begin_fill()

sides = random.randint(3, 12)  # 3~12각형
length = random.randint(50, 150)  # 변 길이 50~150으로 제한
for i in range(sides):
    t.forward(length)
    t.right(360 // sides)
    # 애니메이션 효과
    t.speed(random.randint(1, 5))  # 속도 랜덤

t.end_fill()
# 클릭 시 창 닫기
screen.exitonclick()import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["darkred","yellow","orange","palegreen","cyan","purple","skyblue"]

for i in range(72):
    t.color(colors[i % 7])
    t.circle(100)
    t.left(5)

turtle.done()
import turtle

screen = turtle.Screen()
screen.bgcolor("wheat")  # 배경색 추가
screen.title("My turtle art")
t = turtle.Turtle()
t.pensize(3)
t.color("red","coral")
t.begin_fill()

for i in range(0,10):
    t.right(36)
    for i in range(0,3):
        t.forward(100)
        t.right(120)
t.end_fill()

t.penup()
t.forward(200)
t.pendown()
t.color("red","orange")
t.begin_fill()
for i in range(0,10):
    t.right(36)
    for i in range(0,3):
        t.forward(100)
        t.right(120)
t.end_fill()
turtle.done()import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"포트 {port} 열림")
        sock.close()
    except socket.error as e:
        print(f"포트 {port} 스캔 오류: {e}")

target_host = input("스캔할 호스트 IP 입력 (기본: 127.0.0.1): ") 
for port in range(1, 1025):
    scan_port(target_host, port)import turtle

turtle.bgcolor("lightyellow")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["darkred","yellow","orange","palegreen","coral","purple","skyblue"]

for i in range(72):
   
    t.color(colors[i % 7])
    for _ in range(5):
        t.forward(120)
        t.right(72)
    t.right(7.2)
    
turtle.exitonclick()
import turtle

scr = turtle.Screen()
scr.bgcolor("wheat")
scr.title("My turtle art")

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.color("indigo" ,"lavender")

t.begin_fill()
for i in range(0,8):
    t.forward(100)
    t.left(45)
t.end_fill()

turtle.exitonclick()

import turtle

# 스크린 설정
screen = turtle.Screen()
screen.title("Skyblue Gradient by Ray")

# 배경을 skyblue로 시작
screen.bgcolor("skyblue")

# 터틀 준비
t = turtle.Turtle()
t.speed(0)  # 빠르게 그리기
t.hideturtle()  # 터틀 모양 숨기기

# 그라데이션 효과: 여러 원을 겹쳐 색상 변화
colors = ["lightblue", "skyblue", "lightcyan", "paleturquoise"]  # 밝은 색상 순
for i in range(11):  # 50겹으로 부드럽게
    t.pensize(10 + i)  # 원 테두리 굵기 점진 증가
    t.color(colors[i % 4])  # 색상 순환
    t.circle(100 + i * 2)  # 원 크기 점진 증가
    t.penup()  # 선 안 그리기
    t.goto(0, -100 - i * 2)  # 원 아래로 이동
    t.pendown()  # 그리기 시작

# 창 유지
turtle.done()import turtle
import time

turtle.pensize(3)
turtle.speed(0)
turtle.color("orangered")
# 오각형 그리기
for i in range(50):
    turtle.right(7.2)
    for _ in range(5):
        turtle.forward(120)
        turtle.left(72)
    time.sleep(0.05)
turtle.clear()
# 내부 별 그리기
turtle.penup()
turtle.goto(0,0)   
turtle.pendown()
turtle.speed(0)
turtle.begin_fill()
turtle.color("teal","cyan")
for i in range(50):
    turtle.right(7.2)
    for _ in range(5):
        turtle.forward(170)
        turtle.right(144)   # 별을 그리는 각도
turtle.end_fill()
turtle.done()import turtle
import random
scr = turtle.Screen()
scr.setup(800, 700)
scr.title("My turtle art")
scr.bgcolor("skyblue")
t = turtle.Turtle()
t.shape("circle")
t.speed(3)
try:
    num_circles = (int(input("How many circles? Enter a number: ")))
    if num_circles <= 0:
        print("Please enter a number greater than 0! Using default value of 20.")
        num_circles = 20
    elif num_circles > 30:  # 30개 초과 제한
        print("Maximum 30 circles allowed! Setting to 30.")
        num_circles = 30
except ValueError as e:
    print("Please enter a number! Using default value of 20.",e)
    num_circles = 20

for _ in range(num_circles):
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    colors = random.choice(["gold", "yellow", "crimson", "cyan", "teal", "hotpink", "indigo", "purple"])
    colors2 = random.choice(["crimson", "coral", "plum", "fuchsia", "cyan", "teal", "purple", "darkblue"])
    t.color(colors2, colors)
    t.begin_fill()
    t.circle(random.uniform(5, 25))
    t.end_fill()  # Dual-tone circle at random spot
turtle.exitonclick()import turtle
import random

turtle.bgcolor("black")
turtle.shape("turtle")
turtle.hideturtle()
for _ in range(12):  
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    colors = random.choice(["yellow", "darkorange","coral","orangered","gold","wheat","lightyellow"])
    turtle.color(colors) 
    turtle.begin_fill()
    for _ in range(5):  # 5각 별
        turtle.forward(50)
        turtle.right(144)
    turtle.end_fill()  # 오타 수정
turtle.done()import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.pensize(2)

for i in range(100):
    t.color(0,i/100,i/100)
    for _ in range(6):
        t.forward(100)
        t.right(60)
    t.right(3.6)
t.hideturtle()
turtle.done()
import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(12):
    t.penup()
    t.goto(0, 0)
    t.forward(100)
    t.pendown()
    t.forward(10)
    t.penup()
    t.backward(110)
    t.right(30)

turtle.done()
import turtle
import random
scr = turtle.Screen()
scr.title("My turtle art")
turtle.bgcolor("skyblue")
t = turtle.Turtle()

for _ in range(25):
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    colors = random.choice(["gold", "yellow", "crimson", "cyan", "teal", "hotpink", "indigo", "purple"])
    colors2 = random.choice(["crimson", "coral", "plum", "fuchsia", "cyan", "teal", "purple", "darkblue"])
    t.color(colors2, colors)
    t.begin_fill()
    for _ in range(3):
        t.forward(20)
        t.left(120)
    t.right(10)
    t.end_fill()  
turtle.exitonclick()import turtle
t = turtle.Turtle()

def draw_circle(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    return 3.14 * 50 * 50

area = draw_circle(-130, -70, "gold")
print(f"면적: {area}")  # 결과: 면적: 7850.0

turtle.done()
import socket
import requests
from getmac import get_mac_address


try: 
    hostname = socket.gethostname() # 내 컴퓨터 이름
    ip_address = socket.gethostbyname(hostname) # 내 사설 IP

    ip = requests.get("https://api.ipify.org").text # 공인 IP 호출

    #MAC 주소 
    mac = get_mac_address()

    print("내 컴퓨터 이름", hostname)
    print("내 IP 주소" , ip_address)
    print("공인 IP 주소:", ip)
    print(mac)

    with open("my_network.txt", "w") as f:
        f.write(f"컴퓨터 이름: {hostname}\n")
        f.write(f"IP 주소: {ip_address}\n")
        f.write(f"공인 IP 주소: {ip}\n")
        f.write(f"MAC 주소: {mac}\n")
except Exception as e:
    print("오류 발생", e)
import turtle
import random

turtle.bgcolor("ivory") # 배경색 설정(아이보리)
t = turtle.Turtle()
t.speed(9) # 그림 속도
t.shape("circle") # 커서 모양
colors = ["red", "skyblue","coral", "green", "yellow", "orange", "teal", "purple"] # 색상 리스트

# 원의 위치와 크기를 랜덤 호출하는 함수
def draw_circle():
    #랜덤으로 좌표와 원의 크기, 색상을 선택합니다
    x = random.uniform(-270, 270)
    y = random.uniform(-270, 270)
    radius = random.uniform(10, 80)
    color = random.choice(colors)
    #여기서부터 펜을 들고 원을 그릴 거에요
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

#원을 20개 그립니다
for i in range(20):
    draw_circle()

t.hideturtle()

turtle.exitonclick()import turtle

# 7가지 무지개 색상
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtle.bgcolor("ivory")

# 터틀 설정
turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)  # 시작점: 하단 왼쪽
turtle.pendown()

# --- 하단 줄 (4개 원) ---
for i in range(4):
    turtle.color(colors[i])
    turtle.begin_fill()
    turtle.circle(70)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(140)  # 간격 조정
    turtle.pendown()

# --- 중간 줄 (3개 원) ---
turtle.penup()
turtle.goto(-130,-80)  # 위쪽으로 이동 (살짝 중앙 정렬)
turtle.pendown()

for i in range(4, 7):
    turtle.color(colors[i])
    turtle.begin_fill()
    turtle.circle(70)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(140)
    turtle.pendown()

# --- 상단 줄 (2개 원) ---
turtle.penup()
turtle.goto(-60,40)  
turtle.pendown()

for i in range(2):
    turtle.color(colors[i])
    turtle.begin_fill()
    turtle.circle(70)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(140)
    turtle.pendown()

# --- 상단 줄 (1개 원) ---
turtle.penup()
turtle.goto(10,160)  
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.hideturtle()

turtle.done()from collections import Counter
import string

try:
    # 입력 받기
    new = input("분석할 파일 이름을 넣으세요 예 log.txt : ")

    # 파일 읽기
    with open(new, "r",encoding="utf-8") as file:
        words = [] # 단어를 담을 빈 리스트 생성
        for line in file:
            line = line.strip() 
            line = line.lower() # 소문자변환
            line = line.translate(str.maketrans('', '', string.punctuation)) # 구두점 특수문자 제거
            words.extend(line.split())

    #단어 빈도 계산
    word_counters = Counter(words)
    num = int(input("검사하고 싶은 단어수를 입력하세요. 숫자만 : "))
    #가장 많이 반복된 단어 검사
    top3 = word_counters.most_common(num)

# 파일 분석 결과 출력
    print("--파일 내용 분석--")
    print()
    print(f"자료 전체 분석\n {word_counters}")
    print()
    print(f"가장 빈도 높은 단어 {num}개")
    for word,count in top3:
            print(f" - {word} : {count}회")
    
    
except ValueError:
    print("정확하게 입력하세요")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다")
except IOError as re:
    print("입출력 오류",re)
except (UnicodeDecodeError) as fe:
     print("유니코드 오류", fe)
except Exception as e:
    print("기타 오류" ,e)import sys

print("안녕하세요!")
choice = input("계속할까? (네/아니오): ")
if choice == "아니오":
    print("바이바이!")
    sys.exit()
elif choice != "네":
    print("잘못된 입력! 종료합니다.")
    sys.exit()
print("계속 진행합니다!")
name = input("당신의 이름은? : ")
print(f"안녕? {name}, 만나서 반가워!")

play = input("숫자 맞추기 놀이할까? (Y/N): ").upper()
if play == "N":
    print("잘 가.")
    sys.exit()
elif play != "Y":
    print("Y 또는 N만 입력하세요! 종료합니다.")
    sys.exit()

attempts = 0
max_attempts = 5
while attempts < max_attempts:
    attempts += 1
    try:
        num = int(input("숫자를 입력하시오: "))
        if num == 7 or num == 8:
            print("Correct!")
            break
        else:
            print("Wrong! 다시 시도해!")
            if attempts == max_attempts:
                print("Game over! 5번 실패했어!")
    except ValueError:
        print("숫자만 입력해!")import turtle
turtle.bgcolor("wheat")
t = turtle.Turtle()
t.pensize(3)
t.speed(9)
colors = ["crimson","orange","teal","green","navy","purple","skyblue"]
t.penup()
t.goto(0,-150)
t.pendown()
for i in range(30):
    t.color(colors[i % 7])
    t.circle(i*7+5)

turtle.done()import pygame
import random
import sys

# 초기화
pygame.init()
screen_width, screen_height = 400, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # 청록 (I)
    (255, 255, 0),  # 노랑 (O)
    (128, 0, 128),  # 보라 (T)
    (0, 255, 0),    # 초록 (S)
    (255, 0, 0),    # 빨강 (Z)
    (0, 0, 255),    # 파랑 (J)
    (255, 127, 0)   # 주황 (L)
]

# 배경 그라디언트
def create_gradient_background():
    gradient = pygame.Surface((screen_width, screen_height))
    for y in range(screen_height):
        color = (y // 4, y // 4, 50 + y // 8)
        pygame.draw.line(gradient, color, (0, y), (screen_width, y))
    return gradient

background = create_gradient_background()

# 그리드 설정
grid_size = 40
cols, rows = screen_width // grid_size, screen_height // grid_size
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# 테트로미노 모양
tetrominoes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]]   # L
]

def rotate_tetromino(tetromino):
    return [list(row) for row in zip(*tetromino[::-1])]

class Tetromino:
    def __init__(self):
        self.index = random.randint(0, len(tetrominoes) - 1)
        self.shape = tetrominoes[self.index]
        self.color = COLORS[self.index]
        self.x = cols // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        new_shape = rotate_tetromino(self.shape)
        if not check_collision(self.x, self.y, new_shape):
            self.shape = new_shape

def check_collision(x, y, shape):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                nx, ny = x + j, y + i
                if nx < 0 or nx >= cols or ny >= rows or (ny >= 0 and grid[ny][nx]):
                    return True
    return False

def merge_tetromino(tetromino):
    for i in range(len(tetromino.shape)):
        for j in range(len(tetromino.shape[i])):
            if tetromino.shape[i][j]:
                grid[tetromino.y + i][tetromino.x + j] = tetromino.color

def clear_lines():
    global score
    lines_cleared = 0
    for i in range(rows):
        if all(grid[i]):
            del grid[i]
            grid.insert(0, [0] * cols)
            lines_cleared += 1
    score += lines_cleared * 100
    if lines_cleared > 0:
        line_sound.play()

# 사운드 로드
pygame.mixer.init()
try:
    block_sound = pygame.mixer.Sound('sound_block.wav')
    line_sound = pygame.mixer.Sound('sound_line.wav')
    gameover_sound = pygame.mixer.Sound('sound_gameover.wav')
except FileNotFoundError:
    print("사운드 파일을 찾을 수 없습니다. sound_block.wav, sound_line.wav, sound_gameover.wav를 코드와 같은 폴더에 넣어주세요.")
    block_sound = line_sound = gameover_sound = pygame.mixer.Sound(pygame.mixer.Sound(buffer=bytearray(1000)))

# 사운드 볼륨 조정
block_sound.set_volume(0.5)
line_sound.set_volume(0.7)
gameover_sound.set_volume(0.6)

# 게임 변수
current_tetromino = Tetromino()
score = 0
font = pygame.font.SysFont('Arial', 30, bold=True)
game_over = False
shake_timer = 0
shake_intensity = 0

# 게임 루프
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 500  # ms

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not check_collision(current_tetromino.x - 1, current_tetromino.y, current_tetromino.shape):
                current_tetromino.x -= 1
            if event.key == pygame.K_RIGHT and not check_collision(current_tetromino.x + 1, current_tetromino.y, current_tetromino.shape):
                current_tetromino.x += 1
            if event.key == pygame.K_DOWN:
                fall_speed = 50
            if event.key == pygame.K_UP:
                current_tetromino.rotate()
            if game_over and event.key == pygame.K_r:
                grid = [[0 for _ in range(cols)] for _ in range(rows)]
                current_tetromino = Tetromino()
                score = 0
                game_over = False
                shake_timer = 0

    if not game_over:
        fall_time += clock.get_time()
        if fall_time > fall_speed:
            fall_time = 0
            if not check_collision(current_tetromino.x, current_tetromino.y + 1, current_tetromino.shape):
                current_tetromino.y += 1
            else:
                merge_tetromino(current_tetromino)
                block_sound.play()
                clear_lines()
                current_tetromino = Tetromino()
                if check_collision(current_tetromino.x, current_tetromino.y, current_tetromino.shape):
                    game_over = True
                    gameover_sound.play()
                    shake_timer = 30
                    shake_intensity = 5
            fall_speed = 500

    # 화면 흔들림 효과
    shake_offset_x = random.randint(-shake_intensity, shake_intensity) if shake_timer > 0 else 0
    shake_offset_y = random.randint(-shake_intensity, shake_intensity) if shake_timer > 0 else 0
    if shake_timer > 0:
        shake_timer -= 1

    # 그리드 그리기
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                rect = pygame.Rect(j * grid_size + shake_offset_x, i * grid_size + shake_offset_y, grid_size, grid_size)
                pygame.draw.rect(screen, grid[i][j], rect)
                pygame.draw.rect(screen, (200, 200, 200, 100), rect, 2)

    # 현재 테트로미노 그리기
    for i in range(len(current_tetromino.shape)):
        for j in range(len(current_tetromino.shape[i])):
            if current_tetromino.shape[i][j]:
                rect = pygame.Rect((current_tetromino.x + j) * grid_size + shake_offset_x, (current_tetromino.y + i) * grid_size + shake_offset_y, grid_size, grid_size)
                pygame.draw.rect(screen, current_tetromino.color, rect)
                pygame.draw.rect(screen, (255, 255, 255, 150), rect, 2)

    # 점수 표시
    score_shadow = font.render(f"Score: {score}", True, (50, 50, 50))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_shadow, (12, 12))
    screen.blit(score_text, (10, 10))

    # 게임 오버 화면
    if game_over:
        over_shadow = font.render("Game Over! Press R to Restart", True, (50, 50, 50))
        over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(over_shadow, (screen_width // 2 - 152, screen_height // 2 + 2))
        screen.blit(over_text, (screen_width // 2 - 150, screen_height // 2))

    pygame.display.flip()
    clock.tick(60)import pygame
import random
import sys

# 초기화
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")

# 색상
BLACK = (0, 0, 0)  # 배경
WHITE = (255, 255, 255)  # 공
COLORS = [
    (255, 0, 0),    # 빨강
    (0, 255, 0),    # 초록
    (0, 0, 255),    # 파랑
    (255, 255, 0),  # 노랑
    (255, 165, 0)   # 주황
]

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 20
paddle_speed = 10

# 공 설정
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 4
ball_dy = -4

# 벽돌 설정
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 20
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
        color = COLORS[row % len(COLORS)]  # 행마다 다른 색상
        bricks.append((brick, color))

# 점수 및 폰트
score = 0
font = pygame.font.SysFont('Arial', 24, bold=True)

# 사운드 로드
pygame.mixer.init()
try:
    block_sound = pygame.mixer.Sound('block.wav')  # 벽돌 부수기
    paddle_sound = pygame.mixer.Sound('paddle.wav')  # 패들 충돌
    gameover_sound = pygame.mixer.Sound('gameover.wav')  # 게임 오버
except FileNotFoundError:
    print("사운드 파일(block.wav, paddle.wav, gameover.wav)을 다운로드하세요.")
    block_sound = paddle_sound = gameover_sound = pygame.mixer.Sound(pygame.mixer.Sound(buffer=bytearray(1000)))

block_sound.set_volume(0.5)
paddle_sound.set_volume(0.5)
gameover_sound.set_volume(0.6)

# 게임 루프
clock = pygame.time.Clock()
running = True
game_over = False
game_won = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (game_over or game_won):
            if event.key == pygame.K_r:  # 재시작
                ball_x, ball_y = screen_width // 2, screen_height // 2
                ball_dx, ball_dy = 4, -4
                paddle_x = (screen_width - paddle_width) // 2
                bricks = []
                for row in range(brick_rows):
                    for col in range(brick_cols):
                        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
                        color = COLORS[row % len(COLORS)]
                        bricks.append((brick, color))
                score = 0
                game_over = False
                game_won = False

    if not game_over and not game_won:
        # 키 입력
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # 공 이동
        ball_x += ball_dx
        ball_y += ball_dy

        # 벽 충돌
        if ball_x <= 0 or ball_x >= screen_width - ball_radius * 2:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy
        if ball_y >= screen_height:
            game_over = True
            gameover_sound.play()

        # 패들 충돌
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)
        if ball_rect.colliderect(paddle_rect):
            ball_dy = -ball_dy
            paddle_sound.play()

        # 벽돌 충돌
        for brick, color in bricks[:]:
            if ball_rect.colliderect(brick):
                bricks.remove((brick, color))
                ball_dy = -ball_dy
                score += 10
                block_sound.play()
                break

        # 승리 조건
        if not bricks:
            game_won = True

    # 화면 그리기
    screen.fill(BLACK)  # 검은색 배경

    # 패들 (청록색 그라디언트)
    paddle_surface = pygame.Surface((paddle_width, paddle_height))
    for x in range(paddle_width):
        color = (0, 100 + x, 255 - x // 2)
        pygame.draw.line(paddle_surface, color, (x, 0), (x, paddle_height))
    screen.blit(paddle_surface, (paddle_x, paddle_y))

    # 공 (하얀색, 반짝이는 원)
    ball_surface = pygame.Surface((ball_radius * 2, ball_radius * 2), pygame.SRCALPHA)
    for r in range(ball_radius, 0, -1):
        alpha = 255 - (r * 10)
        pygame.draw.circle(ball_surface, (255, 255, 255, alpha), (ball_radius, ball_radius), r)
    screen.blit(ball_surface, (ball_x, ball_y))

    # 벽돌 (알록달록, 테두리)
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)
        pygame.draw.rect(screen, WHITE, brick, 1)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 게임 오버/승리 화면
    if game_over:
        over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(over_text, (screen_width // 2 - 150, screen_height // 2))
    elif game_won:
        win_text = font.render("You Won! Press R to Restart", True, (0, 255, 0))
        screen.blit(win_text, (screen_width // 2 - 130, screen_height // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("black")

# 터틀 설정
t = turtle.Turtle()
t.speed(0)  # 가장 빠른 속도로 그리기
t.width(1)  # 선의 두께 설정

# 색상 리스트
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]

# 그림 그리기
for i in range(360):
    t.pencolor(colors[i % len(colors)])  # 색상 변경
    t.forward(i * 2)  # 앞으로 이동
    t.right(91)  # 오른쪽으로 91도 회전
    t.circle(i)  # 원 그리기

t.hideturtle()  # 터틀 숨기기
turtle.done()  # 터틀 그래픽 종료�PNG
==은행 거래 내역== 
입금 +2000원, 2025-11-04 21:23:35.150392
출금 +344원, 2025-11-04 21:23:38.746928
출금 +500원, 2025-11-04 21:23:42.054235
최종 잔액 {balance}
==은행 거래 내역== 
은행 거래 시간 {datetime.now}
[입금] +3000원, 2025-11-04 21:32:46.458001
[출금] +2000원, 2025-11-04 21:32:49.988491
[출금] +700원, 2025-11-04 21:32:55.714118
최종잔액 {balance}
==은행 거래 내역== 
은행 거래 시간 {datetime.now}
[입금] +3000원, 2025-11-04 21:32:46.458001
[출금] +2000원, 2025-11-04 21:32:49.988491
[출금] +700원, 2025-11-04 21:32:55.714118
최종잔액 {balance}
==은행 거래 내역== 
은행 거래 시간 {datetime.now}
[입금] +3000원, 2025-11-04 21:32:46.458001
[출금] +2000원, 2025-11-04 21:32:49.988491
[출금] +700원, 2025-11-04 21:32:55.714118
최종잔액 {balance}
==은행 거래 내역== 
은행 거래 시간 {datetime.now}
[입금] +2000원, 2025-11-04 21:34:19.506826
[출금] +233원, 2025-11-04 21:34:22.433388
[출금] +300원, [최종잔액] 1467 2025-11-04 21:34:26.104106
최종잔액 {balance}

==============================
은행 거래 시간: 2025-11-04 21:40:27
==============================
[입금] +1234원, 2025-11-04 21:40:20.802087
[출금] +2000원, [최종잔액] 1234원 2025-11-04 21:40:27.816784
최종 잔액: 1234원
==============================

==============================
은행 거래 시간: 2025-11-04 21:47:47
==============================
[입금] +3000원, 2025-11-04 21:47:38.421409
[출금] +222원, 2025-11-04 21:47:43.120059
[출금] +500원, 2025-11-04 21:47:47.055549
최종 잔액: 2278원
==============================

==============================
은행 거래 시간: 2025-11-04 21:48:51
==============================
[입금] +3000원, 2025-11-04 21:48:45.447308
[출금] +300원, 2025-11-04 21:48:48.897592
[출금] +300원, 2025-11-04 21:48:51.890227
최종 잔액: 2400원
==============================

==============================
은행 거래 시간: 2025-11-04 21:50:48
==============================
[입금] +3000원, 2025-11-04 21:50:40.569054
[출금] +899원, 2025-11-04 21:50:45.306890
[출금] +200원, 2025-11-04 21:50:48.723639
최종 잔액: 1901원
==============================

==============================
은행 거래 시간: 2025-11-04 22:06:05
==============================
[입금] +2000원 | 2025-11-04 22:05:56.344432 2000
[출금] -200원 | 2025-11-04 22:06:00.883796 1800
[출금] -1000원 | 2025-11-04 22:06:05.378002800
최종 잔액: 800원
==============================

==============================
은행 거래 시간: 2025-11-04 22:15:50
==============================

==============================
은행 거래 시간: 2025-11-04 22:18:49
==============================

==============================
은행 거래 시간: 2025-11-04 22:19:34
==============================

==============================
은행 거래 시간: 2025-11-04 22:20:20
==============================

==============================
은행 거래 시간: 2025-11-04 22:24:01
==============================
[입금] +30000원 | 2025-11-04 22:23:52.466511 | 잔액 30000
[출금] -4000원 | 2025-11-04 22:23:56.450821 | 잔액 26000
[출금] -5000원 | 2025-11-04 22:24:01.169062 | 잔액 21000
최종 잔액: 21000원
==============================
RIFF�� WAVEbextZ                                                                                                                                                                                                                                                                                                                                  2007-01-0300:01:54                                                                                                                                                                                                                                                                        Format=PCM,Mode=STEREO,Sample frequency=44100Hz,Size of the sample=16bit ZOOM Handy Recorder H2                                                                                                                                                                 fmt      D�  �   data � � ��r ��N ��O  s  � 	 � ��s u�
 "�{����2�������: _�� ��� 0 � # � ��Z ��D ��_ W � � � =� Pi � ��2 ������O���/��@�^�_�p�w�L���6���w�������� ��)$ �a �� �� W� � ^  � ��9 e����m���t�������S�������}��������h ��%� g>X�� b� � � � X �  $ ����}� ������~�
������� m W � 4 � ��+ ������������ �� w 2 � c d� ^� � l  S ��7 �� ���� =����u�&���p�[���0�������b���� 2 �� !�< /� � ? d \ ��� ��� ��� S * � d�* ��m�7���O�e�����p�G�������������x�����������[  � � o,�p�@z� � S /  ����n���T���H���;� 2�. 0�? �; $�7 ��. f ! .5 �L �? o��� v� ������p�����K��� ��� }�� ;�� �� 8�F ��7 N a � � � � � W O ��% i� $� �	 1���r������� ��< ��4 �� ������ ��. ��8 ��2 Z�. �? *�W w�C ����< ��� ��0��j��ab�2O���!a 53� ~��!��� `�^ c�z ��� ��5 ������O�;���  ��� ��I���}��� ?�d��_)� � ��� �� M�� |�A ��k���g�>�������v���|�� ��c� �� �� #� �S���@
H� �q�)Q� ���0�=����L�����7�S�r���j�1�:���A�; ������ �$���2�mR� �d �  Z ����e���������;�����������s�#�������S"v��G��l�4�6!S� � ��j ���A������R���v��� �9�����y�P���{� �� ��< ��� ` 7� �ny������ CD�� ?�a ��< ��import turtle

# 스크린 설정
screen = turtle.Screen()
screen.setup(width=600, height=600)

# 터틀 설정
t = turtle.Turtle()
t.speed(0)  # 빠른 그리기를 위해 속도를 0으로 설정
t.penup()
t.goto(-300, 300)

# RGB 모드를 255로 설정
screen.colormode(255)

# 하늘 그라데이션 그리기 함수
def draw_sky_gradient(steps):
    # 초기 색상: 짙은 파란색
    r, g, b = 0, 128, 255

    step_height = 600 / steps  # 각 단계별 높이

    for i in range(steps):
        # 위로 갈수록 옅어지는 하늘색 만들기
        r += int((135 - 0) / steps)  # 135는 옅은 하늘색의 빨간색 값
        g += int((206 - 128) / steps)  # 206은 옅은 하늘색의 녹색 값
        b += int((250 - 255) / steps)  # 250은 옅은 하늘색의 파란색 값

        t.fillcolor(r, g, b)
        t.begin_fill()

        # 사각형 그리기 (외곽선을 그리지 않음)
        t.goto(-300, 300 - i * step_height)  # 시작 위치 설정
        t.setheading(0)  # 방향을 오른쪽으로 설정

        # 펜을 들어올려 외곽선이 그려지지 않도록 설정
        t.forward(600)
        t.right(90)
        t.forward(step_height)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(step_height)
        t.right(90)

        t.end_fill()

# 단계 수 설정 (20단계로 그라데이션)
draw_sky_gradient(20)

# 터틀 종료
t.hideturtle()
screen.mainloop()



import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle() 
t.pensize(3) # 도형과 텍스트만 보기 위해 숨김
t.speed(0)      # 빠른 그리기

# 색상 목록
colors = [
     "oldlace", "olive", "olivedrab", "orange", "orangered",
    "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred",
    "papayawhip", "peachpuff", "peru", "pink", "plum",
    "powderblue", "purple", "red", "rosybrown","royalblue",
    "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell"
]




# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이 (원 반지름 30의 2배)
rect_height = 30  # 세로 길이 (원 반지름과 동일)
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(5):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        t.fillcolor(colors[color_idx])  # 색상 채우기
        t.begin_fill()
        for _ in range(2):  # 가로, 세로 반복
            t.forward(rect_width)  # 가로
            t.left(90)
            t.forward(rect_height)  # 세로
            t.left(90)
        t.end_fill()

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))

# 프로그램 종료
turtle.done()import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle() 
t.pensize(3) # 도형과 텍스트만 보기 위해 숨김
t.speed(0)      # 빠른 그리기

# 색상 목록
colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "black", "blanchedalmond", "blue",
    "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse",
    "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson",
    "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray"
]

# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이 (원 반지름 30의 2배)
rect_height = 30  # 세로 길이 (원 반지름과 동일)
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(5):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        t.fillcolor(colors[color_idx])  # 색상 채우기
        t.begin_fill()
        for _ in range(2):  # 가로, 세로 반복
            t.forward(rect_width)  # 가로
            t.left(90)
            t.forward(rect_height)  # 세로
            t.left(90)
        t.end_fill()

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))

# 프로그램 종료
turtle.done()import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle() 
t.pensize(3) # 도형과 텍스트만 보기 위해 숨김
t.speed(0)      # 빠른 그리기

# 색상 목록
colors = [
       "goldenrod", "gray", "grey", "green", "greenyellow",
    "honeydew", "hotpink", "indianred", "indigo", "ivory",
    "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon",
    "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray",
    "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen"
]

# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이 (원 반지름 30의 2배)
rect_height = 30  # 세로 길이 (원 반지름과 동일)
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(5):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        t.fillcolor(colors[color_idx])  # 색상 채우기
        t.begin_fill()
        for _ in range(2):  # 가로, 세로 반복
            t.forward(rect_width)  # 가로
            t.left(90)
            t.forward(rect_height)  # 세로
            t.left(90)
        t.end_fill()

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))

# 프로그램 종료
turtle.done()import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle() 
t.pensize(3) # 도형과 텍스트만 보기 위해 숨김
t.speed(0)      # 빠른 그리기

# 색상 목록
colors = [
     "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid",
    "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray",
    "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
    "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite",
    "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold"
]

# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이 (원 반지름 30의 2배)
rect_height = 30  # 세로 길이 (원 반지름과 동일)
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(5):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        t.fillcolor(colors[color_idx])  # 색상 채우기
        t.begin_fill()
        for _ in range(2):  # 가로, 세로 반복
            t.forward(rect_width)  # 가로
            t.left(90)
            t.forward(rect_height)  # 세로
            t.left(90)
        t.end_fill()

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))

# 프로그램 종료
turtle.done()import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle() 
t.pensize(3) # 도형과 텍스트만 보기 위해 숨김
t.speed(0)      # 빠른 그리기

# 색상 목록
colors = [
    "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow",
    "lime", "limegreen", "linen", "magenta", "maroon",
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue",
    "mintcream", "mistyrose", "moccasin", "navajowhite", "navy","lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow",
    "lime", "limegreen", "linen", "magenta", "maroon",
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue",
    "mintcream", "mistyrose", "moccasin", "navajowhite", "navy"
]

# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이 (원 반지름 30의 2배)
rect_height = 30  # 세로 길이 (원 반지름과 동일)
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(5):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        t.fillcolor(colors[color_idx])  # 색상 채우기
        t.begin_fill()
        for _ in range(2):  # 가로, 세로 반복
            t.forward(rect_width)  # 가로
            t.left(90)
            t.forward(rect_height)  # 세로
            t.left(90)
        t.end_fill()

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))

# 프로그램 종료
turtle.done()import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Colorful Rectangle Grid - Part 3")
turtle.bgcolor("wheat")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.hideturtle()  # 도형과 텍스트만 보기 위해 숨김
t.speed(0)   
t.pensize(3)   # 빠른 그리기

# 색상 목록 (51~65, 나머지 10개는 비움)
colors = [
     "sienna", "silver", "skyblue", "slateblue","yellowgreen",
    "slategray", "slategrey", "snow", "springgreen", "steelblue",
    "tan", "teal", "thistle", "tomato", "turquoise",
    "violet", "wheat", "white", "whitesmoke", "yellow",
   
]

# 그리드 간격 및 직사각형 크기
grid_size = 100  # 각 직사각형 간격
rect_width = 100  # 가로 길이
rect_height = 30  # 세로 길이
start_x = -200   # 시작 x 좌표
start_y = 200    # 시작 y 좌표

# 5x5 그리드에 직사각형 그리기
for row in range(4):
    for col in range(5):
        # 좌표 계산
        x = start_x + col * grid_size
        y = start_y - row * grid_size  # 위에서 아래로
        color_idx = row * 5 + col  # 색상 인덱스

        # 직사각형 그리기
        t.penup()
        t.goto(x - rect_width / 2, y - rect_height / 2)  # 왼쪽 아래 모서리
        t.pendown()
        if color_idx < len(colors) and colors[color_idx]:  # 빈 문자열 제외
            t.fillcolor(colors[color_idx])  # 색상 채우기
            t.begin_fill()
            for _ in range(2):  # 가로, 세로 반복
                t.forward(rect_width)  # 가로
                t.left(90)
                t.forward(rect_height)  # 세로
                t.left(90)
            t.end_fill()
        else:
            t.forward(rect_width)  # 테두리만 그리기
            t.left(90)
            t.forward(rect_height)
            t.left(90)
            t.forward(rect_width)
            t.left(90)
            t.forward(rect_height)

        # 중앙에 색상 이름 쓰기
        t.penup()
        t.goto(x, y - 5)  # 직사각형 중앙 근처 (y 약간 위로 조정)
        if color_idx < len(colors) and colors[color_idx]:
            t.write(colors[color_idx], align="center", font=("Arial", 10, "normal"))
        else:
            t.write("N/A", align="center", font=("Arial", 10, "normal"))  # 빈 경우 표시

# 프로그램 종료
turtle.done()# This password checker is safe and block the danger.
# Note: uses "decoy" for fake examples and keeps an "audit" trail in the log.
# Use shell to set flag on decoy hit.
# "Decoy" entries may be used for testing, but do not affect real blocking decisions.
# Critical alerts are flagged and recorded for further review.
# Beacon vs Rootkit: signals are visible, hidden threats are exposed.
# Payload and Tunneling: payload is the content, tunneling is the hidden path.
# Hackers exploit vulnerabilities in the system through backdoor.
# Warning: intrusion and obfuscation

from datetime import datetime

checked_count = 0  # Counter for checked emails
seen_emails = set()

def log_action(action, email):
    with open("email_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} |{action}| {email} |Emails checked={checked_count}\n")


def log_decoy_details(email):
    log_action(f"Beacon: {email} active", email)
    log_action("OSINT: Port 80 open on target", email)
    log_action("Scan: Target IP 192.168.1.1 open", email)

while True:
    try:
        email = input("Enter an email: ").lower()
    except Exception as e:
        print(f"Input error: {e}")
        continue
    
    if email == "stop":
        print("Program ended.")
        print(f"Emails checked: {checked_count}")
        log_action("Program ended", email)
        break

    checked_count += 1

    if email in seen_emails:
        print("Duplicate detected.")
        log_action("Duplicate detected", email)
    else:
        seen_emails.add(email)

    if '@' not in email:
        print("Invalid format!")
        log_action("Invalid format", email)
    elif email == "decoy@trap.com":
        print("Decoy triggered!")
        log_action("Decoy triggered", email)
        log_decoy_details(email)
    elif len(email) < 5:
        print("Too short!")
        log_action("Too short!", email)
    elif len(email) >= 50:
        print("Too long! Possible spoof!")
        log_action("Possible spoof", email)
    elif "bank" in email or "login" in email:
        print("Danger!")
        log_action("Danger", email)
    else:
        print("Safe.")
        log_action("Safe", email)# digital_clock.py
import tkinter as tk
from datetime import datetime


# 1. 창 설정
root = tk.Tk()
root.title("Ray의 디지털 시계")
root.geometry("500x200")
root.resizable(False, False)
root.configure(bg="#1a1a1a")  # 어두운 배경


# 2. 폰트 설정
time_font = ("DS-Digital", 68, "bold")
date_font = ("Helvetica", 20)


# 3. 라벨 생성-
time_label = tk.Label(
    root,
    font=time_font,
    bg="#080808",
    fg="#00ffae",  # 네온 그린
    text="00:00:00"
)
time_label.pack(expand=True)

date_label = tk.Label(
    root,
    font=date_font,
    bg="#1a1a1a",
    fg="#7B65F4",
    text="YYYY-MM-DD DAY"
)
date_label.pack()


# 4. 시간 업데이트 함수
def update_clock():
    now = datetime.now()
    
    # 시간 (24시간제)
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    
    # 날짜 + 요일
    weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    current_date = now.strftime("%Y-%m-%d") + " " + weekdays[now.weekday()]
    date_label.config(text=current_date)
    
    # 1초 후 다시 호출
    root.after(1000, update_clock)


# 5. 시작
update_clock()
root.mainloop()import turtle
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
turtle.done()2025-09-29 09:39:14.531260 |Safe| & c:/users/user/appdata/local/programs/python/python313/python.exe c:/python/007.py
2025-09-29 09:39:24.596937 |Safe| help
2025-09-29 09:39:33.745979 |Danger| bank
2025-09-29 09:39:38.648421 |Program ended| stop
2025-09-29 09:43:48.132076 |Safe| help
2025-09-29 09:43:53.508974 |Danger| bank
2025-09-29 10:12:23.943342 |Safe| blue sky
2025-09-29 10:12:28.804381 |Danger| login
2025-09-29 10:12:32.442192 |Program ended| stop
2025-09-30 09:34:46.673813 |Safe| sdfl;kkjfkjlgkjldkjakjafklafs
2025-09-30 09:35:00.422458 |Possible spoof| ddjkjkjkjjkjkdfjffdjkfjjjfdajfadfkfdjfkdkjfkdjfkjdfkjdk;fj;kdjf;kdjfk;jd;kfjkasdjf;kjdf;kjfaj;r;kh;ktjkhr;kjr;kjr
2025-09-30 09:35:14.441236 |Danger| login 
2025-09-30 09:35:21.457078 |Program ended| stop
2025-09-30 09:41:02.171616 |Possible spoof| kjdfkjlldfkjkfddddddddddddddddddddddddddddddddddddaweknknwavancaerrrrr
2025-09-30 09:41:07.852359 |Danger| login
2025-09-30 09:41:12.220024 |Program ended| stop
2025-09-30 09:48:04.457551 |Possible spoof| kjdkjfkdfkjadfjadhf;jhdajgh;a;hgjhdfgjdhjhfjdhjkah
2025-09-30 09:48:26.789629 |Safe| dkslf
2025-09-30 09:48:31.805047 |Danger| login
2025-09-30 09:48:35.767953 |Program ended| stop
2025-10-01 09:53:26.843258 |Safe| dkjdkfjlkdfjkdjfkaljfkdaljfkdalfjklddddddddd
2025-10-01 09:53:35.059758 |Danger| bank
2025-10-01 09:53:40.852594 |Safe| ㄹㄹㄷㄷㄷㄹㄹ
2025-10-01 09:53:55.622886 |Possible spoof| 어리ㅏㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㄹㄹㄹㄹ러러러ㅓ러러ㅓㅏㅇㅇㅇㅇㅇㅇㅇㅇㅇ임러뒤ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
2025-10-01 09:54:16.246029 |Program ended| stop |Emails checked=4
2025-10-01 09:55:10.746795 |Possible spoof| kjjejfkadjvkljdkja;ghiekjnnkdjfkaaasq@eqqqqqfjdkaaaaal;jfdkallllllllldda;
2025-10-01 09:55:38.908422 |Safe| beebusyflying
2025-10-01 09:55:45.335224 |Safe| long
2025-10-01 09:55:54.421642 |Program ended| stop |Emails checked=3
2025-10-01 09:56:16.926526 |Possible spoof| ddkjfkdajkfajkelffffw ;vjewvwwjfdkalllllllllllllllllllllllllllfjeeeeeeeeeeen
2025-10-01 09:56:29.689234 |Safe| beebusyflying
2025-10-01 09:56:37.246485 |Danger| bank
2025-10-01 09:56:56.588299 |Safe| what is honeypot?
2025-10-01 09:57:05.056359 |Program ended| stop |Emails checked=4
2025-10-02 09:44:00.062341 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-02 09:44:08.965365 |Possible spoof| fdjhfjas;kdskfddkldfjkkfjiejklejklandlvndjhweioarieqwhfehfklasejkbthhkea
2025-10-02 09:44:21.501473 |Safe| good
2025-10-02 09:44:33.297866 |Danger| bankloing
2025-10-02 09:45:09.240724 |Danger| banklogin
2025-10-02 09:45:15.703391 |Program ended| stop |Emails checked=5
2025-10-02 11:54:59.980087 |Invalid format| fddjhfdsahfjdhfjh;d |Emails checked=1
2025-10-02 11:55:09.453975 |Invalid format| djhaflhjhdfhjfhjdlasfklhfjhdfljhjfhdjlfhjdkhfjdhfjkdhfjdhlfjdhjfjdfhdjfhldjkhlfasj |Emails checked=2
2025-10-02 11:55:22.266563 |Possible spoof| djddkdkdk@kjdlzxcvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvedrvnnnnndkljllvsvkdkdlkdldkl
2025-10-02 11:55:37.725789 |Danger| bank@com
2025-10-02 11:55:53.264102 |Safe| my email@com
2025-10-02 11:55:58.406097 |Program ended| stop |Emails checked=5
2025-10-03 09:56:53.718530 |Possible spoof| jfkajsdkjfkawj;kejrkj;gighfjgjkjjewikerkejktjknkrnkerjakjrkl2@dkfajkdj
2025-10-03 09:57:01.841547 |Safe| safe@
2025-10-03 09:57:06.928043 |Duplicate detected| safe@ |Emails checked=3
2025-10-03 09:57:06.929473 |Safe| safe@
2025-10-03 09:57:11.277139 |Invalid format| kdjkfjkwejakjrkr |Emails checked=4
2025-10-03 09:57:20.680163 |Program ended| stop |Emails checked=4
2025-10-04 10:04:36.829568 |Invalid format| decoy |Emails checked=1
2025-10-04 10:04:46.396409 |Safe| decoy@com |Emails checked=2
2025-10-04 10:05:00.362889 |Possible spoof| jjkewjkr fhfdkweaehrbc;jfjhd;fakfelkwrjbjaebajh;hahejnj@ |Emails checked=3
2025-10-04 10:05:04.479759 |Invalid format| #$ |Emails checked=4
2025-10-04 10:05:17.998305 |Danger| login@ |Emails checked=5
2025-10-04 10:05:26.050641 |Program ended| stop |Emails checked=5
2025-10-04 10:05:52.769411 |Invalid format| decoy |Emails checked=1
2025-10-04 10:05:57.794976 |Safe| decoy@ |Emails checked=2
2025-10-04 10:06:01.749218 |Duplicate detected| decoy@ |Emails checked=3
2025-10-04 10:06:01.750837 |Safe| decoy@ |Emails checked=3
2025-10-04 10:06:09.949229 |Possible spoof| dkjfkdajkerjktj;kjfkdgkgjjrt;ktkjtkj;skj;gkjgkjs;erktjkt@ |Emails checked=4
2025-10-04 10:06:17.903485 |Danger| bank@com |Emails checked=5
2025-10-04 10:06:21.353613 |Program ended| stop |Emails checked=5
2025-10-05 09:56:57.258526 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-05 09:56:57.270628 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-05 09:57:08.218154 |Invalid format| danger |Emails checked=2
2025-10-05 09:57:16.784250 |Danger| bank@com |Emails checked=3
2025-10-05 09:57:29.291238 |Possible spoof| dfkjkejkjkejkajfkjkgjfjgkfjgkajkwejrkatkankgakjgkjkrjkarjkjkjtkajajtkjk@ |Emails checked=4
2025-10-05 09:57:33.949990 |Program ended| stop |Emails checked=4
2025-10-06 09:45:47.895365 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-06 09:45:47.898357 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-06 09:45:47.900106 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-06 09:45:54.118890 |Danger| bank@ |Emails checked=2
2025-10-06 09:46:01.159806 |Safe| dkjkejekjfjfkdajfoetntnklajfaiwqntjtnkjakjkfjeja@ |Emails checked=3
2025-10-06 09:46:13.018985 |Safe| safe@com |Emails checked=4
2025-10-06 09:46:39.211646 |Program ended| stop |Emails checked=5
2025-10-07 09:41:55.230102 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-07 09:41:55.231425 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-07 09:41:55.232421 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-07 09:41:55.233667 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-07 09:42:01.659811 |Safe| safe@ |Emails checked=2
2025-10-07 09:42:09.023646 |Danger| bank@com |Emails checked=3
2025-10-07 09:42:18.182631 |Possible spoof| ddjfkejntk;jdjkgkjgkdjgkjkerjtkejtkjkjkerjtkrjkrjtkjrktjkjtkrejkjk@ |Emails checked=4
2025-10-07 09:42:26.824698 |Duplicate detected| safe@ |Emails checked=5
2025-10-07 09:42:26.825799 |Safe| safe@ |Emails checked=5
2025-10-07 09:42:31.094836 |Program ended| stop |Emails checked=5
2025-10-07 10:04:13.900736 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-07 10:04:13.901682 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-07 10:04:13.902689 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-07 10:04:13.904057 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-07 10:04:33.528466 |Possible spoof| dfkjllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll@ |Emails checked=3
2025-10-07 10:04:49.846020 |Safe| safe@ |Emails checked=4
2025-10-07 10:04:54.097559 |Duplicate detected| safe@ |Emails checked=5
2025-10-07 10:04:54.098562 |Safe| safe@ |Emails checked=5
2025-10-07 10:04:59.043573 |Invalid format| bank |Emails checked=6
2025-10-07 10:05:25.821255 |Invalid format| python007.py |Emails checked=7
2025-10-07 10:05:35.648128 |Duplicate detected| decoy@trap.com |Emails checked=8
2025-10-07 10:05:35.649224 |Decoy triggered| decoy@trap.com |Emails checked=8
2025-10-07 10:05:35.649921 |Beacon: decoy@trap.com active| Emails checked=8
2025-10-07 10:05:35.650711 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=8
2025-10-07 10:05:35.651557 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=8
2025-10-07 10:05:39.782417 |Duplicate detected| dd@ |Emails checked=9
2025-10-07 10:05:45.186846 |Duplicate detected| dd@ |Emails checked=10
2025-10-07 10:06:03.208023 |Program ended| stop |Emails checked=10
2025-10-07 10:07:17.583021 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-07 10:07:17.583917 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-07 10:07:17.584498 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-07 10:07:17.585749 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-07 10:07:31.882688 |Safe| safe@ |Emails checked=3
2025-10-07 10:07:39.108927 |Danger| bank@ |Emails checked=4
2025-10-07 10:07:50.677828 |Safe| dot@com |Emails checked=5
2025-10-07 10:07:57.069321 |Duplicate detected| dot@com |Emails checked=6
2025-10-07 10:07:57.070408 |Safe| dot@com |Emails checked=6
2025-10-07 10:09:34.517777 |Safe| dot@emile |Emails checked=7
2025-10-07 10:10:24.619974 |Duplicate detected| dot@emile |Emails checked=8
2025-10-07 10:10:24.621522 |Safe| dot@emile |Emails checked=8
2025-10-07 10:10:36.420781 |Program ended| stop |Emails checked=8
2025-10-07 10:14:39.114753 |Safe| dot@emile |Emails checked=2
2025-10-07 10:14:42.256199 |Duplicate detected| dot@emile |Emails checked=3
2025-10-07 10:14:42.258165 |Safe| dot@emile |Emails checked=3
2025-10-07 10:15:12.519763 |Danger| bank@ |Emails checked=4
2025-10-07 10:16:16.045484 |Safe|  decoy@trap.com |Emails checked=5
2025-10-07 10:16:21.014079 |Program ended| stop |Emails checked=5
2025-10-07 10:17:35.973513 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-07 10:17:35.974413 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-07 10:17:35.975481 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-07 10:17:35.976748 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-07 10:17:52.847960 |Safe| dot@emile |Emails checked=3
2025-10-07 10:17:57.060483 |Duplicate detected| dot@emile |Emails checked=4
2025-10-07 10:17:57.061699 |Safe| dot@emile |Emails checked=4
2025-10-07 10:18:05.125834 |Danger| bank@ |Emails checked=5
2025-10-07 10:18:09.128810 |Program ended| stop |Emails checked=5
2025-10-07 10:21:44.027558 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-07 10:21:44.028826 |Beacon: decoy@trap.com active| Emails checked=1
2025-10-07 10:21:44.030140 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-07 10:21:44.031083 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-07 10:22:04.892659 |Safe| dot@emile |Emails checked=3
2025-10-07 10:22:11.776555 |Duplicate detected| dot@emile |Emails checked=4
2025-10-07 10:22:11.777801 |Safe| dot@emile |Emails checked=4
2025-10-07 10:22:19.600392 |Danger| bank@ |Emails checked=5
2025-10-07 10:22:22.934268 |Program ended| stop |Emails checked=5
2025-10-09 09:43:35.529179 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-09 09:43:35.530556 |Beacon: decoy@trap.com active| decoy@trap.com |Emails checked=1
2025-10-09 09:43:35.531193 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-09 09:43:35.532361 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-09 09:43:45.089557 |Too short!| ad@ |Emails checked=2
2025-10-09 09:43:54.738010 |Danger| bank@ |Emails checked=3
2025-10-09 09:44:06.815203 |Duplicate detected| ad@ |Emails checked=4
2025-10-09 09:44:06.816406 |Too short!| ad@ |Emails checked=4
2025-10-09 09:44:13.063050 |Program ended| stop |Emails checked=4
2025-10-09 09:44:33.171700 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-09 09:44:33.172585 |Beacon: decoy@trap.com active| decoy@trap.com |Emails checked=1
2025-10-09 09:44:33.173872 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-09 09:44:33.175038 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-09 09:44:38.667924 |Too short!| ad@ |Emails checked=2
2025-10-09 09:44:40.431351 |Duplicate detected| ad@ |Emails checked=3
2025-10-09 09:44:40.432495 |Too short!| ad@ |Emails checked=3
2025-10-09 09:44:45.389313 |Danger| bank@ |Emails checked=4
2025-10-09 09:45:06.715194 |Safe| lalalal@com |Emails checked=5
2025-10-09 09:45:10.245035 |Program ended| stop |Emails checked=5
2025-10-09 09:50:06.245588 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-09 09:50:06.246583 |Beacon: decoy@trap.com active| decoy@trap.com |Emails checked=1
2025-10-09 09:50:06.247779 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-09 09:50:06.248421 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-09 09:50:14.418960 |Too short!| ad@ |Emails checked=2
2025-10-09 09:50:16.314132 |Duplicate detected| ad@ |Emails checked=3
2025-10-09 09:50:16.315313 |Too short!| ad@ |Emails checked=3
2025-10-09 09:50:23.118951 |Safe| lalalal@com |Emails checked=4
2025-10-09 09:50:28.023789 |Danger| bank@ |Emails checked=5
2025-10-09 09:50:30.752181 |Program ended| stop |Emails checked=5
2025-10-09 09:57:53.376877 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-09 09:57:53.377714 |Beacon: decoy@trap.com active| decoy@trap.com |Emails checked=1
2025-10-09 09:57:53.378345 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-09 09:57:53.379158 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-09 09:57:56.217829 |Too short!| ad@ |Emails checked=2
2025-10-09 09:57:58.640972 |Duplicate detected| ad@ |Emails checked=3
2025-10-09 09:57:58.642195 |Too short!| ad@ |Emails checked=3
2025-10-09 09:58:11.722482 |Program ended| stop |Emails checked=3
2025-10-09 09:58:38.665139 |Too short!| ad@ |Emails checked=1
2025-10-09 09:58:40.419495 |Duplicate detected| ad@ |Emails checked=2
2025-10-09 09:58:40.420932 |Too short!| ad@ |Emails checked=2
2025-10-09 09:58:47.698628 |Invalid format| dkjfjjkr |Emails checked=3
2025-10-09 09:58:55.336797 |Danger| bank@ |Emails checked=4
2025-10-09 09:59:02.733043 |Program ended| stop |Emails checked=4
2025-10-09 09:59:28.092275 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-09 09:59:28.093353 |Beacon: decoy@trap.com active| decoy@trap.com |Emails checked=1
2025-10-09 09:59:28.094004 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-09 09:59:28.094533 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-09 09:59:32.008593 |Too short!| ad@ |Emails checked=2
2025-10-09 09:59:33.615139 |Duplicate detected| ad@ |Emails checked=3
2025-10-09 09:59:33.616355 |Too short!| ad@ |Emails checked=3
2025-10-09 09:59:35.587824 |Invalid format| djhfnee |Emails checked=4
2025-10-09 09:59:40.010871 |Danger| bank@ |Emails checked=5
2025-10-09 09:59:45.453339 |Program ended| stop |Emails checked=5
2025-10-09 10:02:27.757131 |Decoy triggered| decoy@trap.com |Emails checked=1
2025-10-09 10:02:27.758279 |Beacon: decoy@trap.com active| decoy@trap.com |Emails checked=1
2025-10-09 10:02:27.759207 |OSINT: Port 80 open on target| decoy@trap.com |Emails checked=1
2025-10-09 10:02:27.760141 |Scan: Target IP 192.168.1.1 open| decoy@trap.com |Emails checked=1
2025-10-09 10:02:35.110764 |Too short!| bb@ |Emails checked=2
2025-10-09 10:02:37.139954 |Duplicate detected| bb@ |Emails checked=3
2025-10-09 10:02:37.141014 |Too short!| bb@ |Emails checked=3
2025-10-09 10:02:43.537545 |Possible spoof| kajfkjkadg;klfgjkrjkjkrjtkrjkj;ykjkjkjkr;jkrjkrjkrjkrnker@ |Emails checked=4
2025-10-09 10:02:48.186100 |Danger| bank@ |Emails checked=5
2025-10-09 10:02:50.699763 |Program ended| stop |Emails checked=5
import random
num = random.randint(1,10)
correct = False
attempts = 0
max_attempts = 3
while correct == False and attempts < max_attempts:
    try:
        guess = int(input("Enter a number(you have only three attempts) : "))
        attempts += 1
        if guess == num:
            print("Correct!")
            correct = True
        elif guess > num:
            print("Too high. Try again!")
        else:
            print("Too low. Try again!")
    except ValueError:
        print("You can enter only a number.")
    if attempts == 3:
            print("Game over! Number was",num)
import turtle

turtle.bgcolor("cornsilk")
t = turtle.Turtle()
t.pensize(2)
t.speed(0)
colors = ["blue", "skyblue", "gold", "lime", "springgreen","teal", "seagreen"]

for i in range(72):
    t.color(colors[i % 7])
    for _ in range(5):
        t.forward(120)
        t.right(72)
    t.right(5)

turtle.done()


import turtle
turtle.bgcolor("wheat")
t = turtle.Turtle()
t.pensize(3)
t.speed(8)
colors = ["crimson","orange","teal","green","navy","purple","skyblue"]
t.penup()
t.goto(180,-180)
t.pendown()
for i in range(30):
    t.color(colors[i % 7])
    for j in range(4):
        t.forward(j*7+5)
        t.right(90)

for i in range(4):
        t.forward(430)
        t.right(90)
t.hideturtle()
turtle.exitonclick()RIFF*� WAVEfmt      D�  �   data��   �� ����  ������  ����  ���� 	 ����   �� 
   ����
 	 ����  ���� 
  ����	  ������  ���� ����  ����  ����  ����  �� ����   �� 	 ����	  ����  �� ������  ����  ����  �� 
           &     '     	    ������
  ������������������������������       "   ' &  ! 2 &     ��    " &  2 8 0 ' 2025-09-24 19:43:08.228654 ERROR = string index out of range 
2025-09-24 19:43:18.267668 REVERSE NAME = ray GREET = Hello, yar!
2025-09-24 19:43:33.072413 REVERSE NAME = Jhon GREET = Hello, ohJ!
2025-09-24 19:45:58.564243 REVERSE NAME = Ray GREET = Hello, yaR!
2025-09-24 19:58:32.477110 REVERSE NAME = Ray GREET = Hello, yaR!
2025-09-24 19:58:40.703177 REVERSE NAME = Grok GREET = Hello, orG!
2025-09-24 20:05:48.351487 | REVERSE NAME | = Ray | GREET | = Hello, yaR!
2025-09-24 20:06:11.816440 | REVERSE NAME | = Grok | GREET | = Hello, orG!
2025-09-24 20:09:43.917332 | REVERSE NAME | = Ray | GREET | = Hello, yaR!
2025-09-24 20:09:52.457509 | REVERSE NAME | = Hi | GREET | = 세 글자 이상 입력하세요!
2025-09-24 20:10:17.203690 | REVERSE NAME | = Grok | GREET | = Hello, orG!
2025-09-24 20:19:01.779386 | NAME | = Ray | GREET | = Hello, Ray!
2025-09-24 20:19:10.968625 | NAME | = Hi | ERROR | = 세 글자 이상 입력하세요!
2025-09-24 20:19:18.589949 | NAME | = Grok | GREET | = Hello, Gro!
2025-09-24 20:30:12.589673 | name | = Ray | greet | = Hello, yaR!
2025-09-24 20:30:29.494558 | name | = Hi | error | = 세 글자 이상 입력하세요!
2025-09-24 20:30:35.775307 | name | = Grok | greet | = Hello, orG!
2025-09-24 21:02:24.951428 | name | = Ray | greet | = Hello, yaR!
2025-09-24 21:05:56.821387 | name | = ray | greet | = Hello, yar!
2025-09-24 21:06:26.666486 | name | = hi | error | = 세 글자 이상 입력하세요!
2025-09-24 21:06:52.467929 | name | = cat | greet | = Hello, tac!
2025-09-24 21:08:07.498265 | name | = Ray | greet | = Hello, yar!
2025-09-24 21:08:15.305651 | name | = Hi | error | = 세 글자 이상 입력하세요!
2025-09-24 21:08:35.269842 | name | = Cat | greet | = Hello, tac!
import turtle

turtle.bgcolor("cornsilk")

t=turtle.Turtle()

t.color('red')
t.begin_fill()
t.left(45)
t.forward(200)
t.circle(73, 221.3)

t.left(180)
t.circle(73, 221.3)

t.forward(200)
t.end_fill()

turtle.exitonclick()
from datetime import datetime
try:
    password = input("Enter password: ")
    if len(password) >= 8:
        print("Secure!")
        with open("C:/python/log.txt", "a", encoding="UTF-8") as file:  # 절대 경로 지정
            file.write(f"{datetime.now()}: Secure password\n")
    else:
        print("Weak!")
        with open("C:/python/log.txt", "a", encoding="UTF-8") as file:  # 절대 경로 지정
            file.write(f"{datetime.now()}: Weak password\n")
except Exception:
    print("적합하지 않습니다.")import random

def encrypt(text):
    result = ""
    keys = []  # 각 문자마다 난수 키 저장
    for j in text:
        key = random.randint(1, 10)  #  문자마다 1~10 사이의 난수 키 생성
        keys.append(key)
        result += chr(ord(j) + key)
    return result, keys


def decrypt(encrypted, keys):
    decrypted = ""
    for i, char in enumerate(encrypted):
        decrypted += chr(ord(char) - keys[i])
    return decrypted



word = input("암호화할 단어: ")
encrypted, keys = encrypt(word)

print("암호화 결과")
print("암호화된 단어:", encrypted)
print("사용된 키 목록:", keys)

decrypted = decrypt(encrypted, keys)
print("복호화된 단어:", decrypted)2025-09-19 00:38:52.846699: Secure password
2025-09-19 00:38:57.907712: Weak password
2025-09-19 00:39:04.026034: Secure password
2025-09-19 18:51:41.360898: Weak password
2025-09-19 18:52:00.439419: Secure password
2025-09-19 19:05:59.307086: Secure password
2025-09-21 23:09:25.137128: Secure password
2025-09-21 23:10:15.827602: Weak password
2025-09-22 00:00:19.336303: Secure password
2025-09-23 20:30:01.412966 | ABS | input=20.0 | output=20.0
2025-09-23 20:30:16.812916 | ABS | input=-2.45 | output=2.45
2025-09-23 20:30:25.431226 | ABS | input=-0.235 | output=0.235
2025-09-23 20:30:50.078396 | ABS | input=-3.0 | output=3.0
2025-09-23 20:30:54.444595 | ABS | input=5.5 | output=5.5
2025-09-23 20:31:00.181818 | ERROR | could not convert string to float: 'abc'
2025-09-23 22:02:44.102059 | ABS | input=33.0 | output=33.0
2025-09-23 22:04:02.376805 | ABS | input=334.7 | output=334.7
2025-09-23 22:04:27.977413 | ERROR | could not convert string to float: ''
2025-09-23 22:04:44.315819 | ABS | input=0.0 | output=0.0
2025-09-23 22:04:58.136296 | ERROR | could not convert string to float: ''
2025-09-23 22:05:25.325965 | ABS | input=-3.0 | output=3.0
2025-09-23 22:05:39.134905 | ABS | input=5.5 | output=5.5
2025-09-23 22:05:47.866360 | ERROR | could not convert string to float: 'abc'
2025-09-23 22:26:50.941691 | ABS | input=22.0 | output=22.0
2025-09-23 22:27:03.016187 | ABS | input=-4.0 | output=4.0
2025-09-23 22:27:12.175036 | ERROR |
2025-09-23 22:33:35.213008 | ERROR| could not convert string to float: 'dd' 
2025-09-25 18:47:15.632218 |TRY AGAIN| = 3
2025-09-25 18:47:17.078735 |ERROR| = invalid literal for int() with base 10: 'd'
2025-09-25 18:47:18.514111 |TRY AGAIN| = 1
2025-09-25 18:47:21.309022 |TRY AGAIN| = 2
2025-09-25 18:48:50.438165 |TRY AGAIN| = 3
2025-09-25 18:48:51.760826 |ERROR| = invalid literal for int() with base 10: 'd'
2025-09-25 18:48:53.374004 |CORRECT| = 7
2025-09-25 18:52:26.035877 |GOOD| = 5
2025-09-25 18:52:28.637502 |CORRECT| = 6
2025-09-25 19:02:18.549476 |TRY AGAIN| = 3
2025-09-25 19:02:20.639243 |GOOD| = 5
2025-09-25 19:02:22.929298 |CORRECT| = 7
2025-09-25 19:02:35.210017 |ERROR| = invalid literal for int() with base 10: 'abc'
2025-09-25 19:02:39.200938 |ERROR| = invalid literal for int() with base 10: 'n'
2025-09-25 19:04:00.953807 |GOOD| = 5
2025-09-25 19:04:05.400737 |CORRECT| = 9
2025-09-25 19:13:34.558955|ERROR=invalid literal for int() with base 10: 'y'|
2025-09-25 19:13:45.785335|ERROR=invalid literal for int() with base 10: 'y'|
2025-09-25 19:14:04.195303|ERROR=invalid literal for int() with base 10: 'n'|
2025-09-25 19:14:18.403761|ERROR=invalid literal for int() with base 10: 'n'|
2025-09-25 19:15:25.329960|TRY AGAIN=3|
2025-09-25 19:15:36.242795|GOOD=5|
2025-09-25 19:15:43.322732|CORRECT=7|
2025-09-22 00:56:40.085260 | REVERSE | input=dd | output=['dd']
2025-09-22 00:56:57.042576 | REVERSE | input=�ȳ��ϼ��� | output=['�ȳ��ϼ���']
2025-09-22 01:03:59.216860 | REVERSE | input=안녕하세요 | output=['안녕하세요']
2025-09-22 01:04:05.650688 | REVERSE | input=그록은 너무 엄격해 | output=['그록은', '너무', '엄격해']
2025-09-22 01:04:15.197945 | REVERSE | input=조금만 살살해주세요~~ | output=['조금만', '살살해주세요~~']
2025-09-22 01:04:37.336269 | REVERSE | input=삼촌, 제발 | output=['삼촌,', '제발']
2025-09-22 01:23:07.623300 | REVERSE | input=하이 그록? | output=그록? 하이!
2025-09-22 01:23:18.867604 | REVERSE | input=날씨가 너무 좋아요' | output=좋아요' 너무 날씨가!
2025-09-22 01:24:05.661549 | REVERSE | input=& C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe c:/python/002.py | output=c:/python/002.py C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe &!
2025-09-22 01:24:16.137358 | REVERSE | input=2 | output=2!
2025-09-22 01:24:28.127762 | REVERSE | input=@ | output=@!
2025-09-22 01:29:58.144567 | ERROR | 단어가 없습니다.
2025-09-22 01:31:42.162365 | ERROR | 단어가 없습니다.
2025-09-23 20:21:21.876368 | REVERSE | input=안녕하세요. 레이입니다 | output=레이입니다 안녕하세요.!
2025-09-26 13:49:26.485029 |dangerous| 192.168.1.1
2025-09-26 13:49:39.808121 |clean| 8.8.8.8
2025-09-26 13:58:23.342484 |clean| & C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe c:/python/007.py
2025-09-26 13:58:41.163939 |dangerous| 10.0.0.1
2025-09-26 13:59:34.084138 |clean| 8.8.8.8
2025-09-26 14:10:09.009761 |clean| 8.8.8.8
2025-09-26 14:10:28.840340 |dangerous| 10.0.0.1
2025-09-26 14:10:39.423814 |dangerous| 192.168.1.1
2025-09-26 14:20:14.884918 |dangerous| 10.0.0.1
2025-09-26 14:20:28.745332 |dangerous| 192.168.1.1
2025-09-26 14:26:57.458186|dangerous=192.168.1.1|
2025-09-26 14:27:07.659505|dangerous=10.0.0.1|
2025-09-26 14:40:01.758522|dangerous=192.168.1.1|
2025-09-26 14:40:13.308506|dangerous=10.0.0.1|
2025-09-26 14:44:26.132028|dangerous=192.168.1.1|
2025-09-26 14:44:48.015767|dangerous=192.168.1.1|
2025-09-26 14:44:57.177886|dangerous=10.0.0.1|
import turtle as t
import random

# 배경 설정
t.title("My Turtle Art")
t.bgcolor("ivory") # 배경을 부드러운 아이보리색으로 설정
t.speed(0) # 그리기 속도는 최대로
t.colormode(255) # RGB 색상모드를 0~255로 설정
t.hideturtle() # 커서 숨기기

# 100개의 점을 무작위로 그리기
for i in range(100):
    # 무작위로 RGB 색상 생성
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    # 무작위 위치 설정(x,y 좌표)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    # 무작위 크기 설정(15~30 픽셀)
    size = random.randint(15, 30)
    # 점 찍을 위치 준비 및 이동
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 점의 사이즈 및 색상 지정
    t.dot(size,(r, g, b))

# 클릭으로 창 종료
t.exitonclick()import turtle

scr =turtle.Screen()
scr.setup(800, 700)  # 화면 크기 설정
scr.bgcolor("wheat") # 배경색
scr.title("My turtle Art") # 제목

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(9)
t.hideturtle() # 커서 숨김

t.penup() # 펜 들어
t.goto(-175,0) # -175,0 좌표로 이동
t.pendown() # 펜 내려

colors = ["orange", "red", "orangered", "salmon", "crimson", "coral", "darkorange"] # 사용할 색상을 리스트에 담아줌

for i in range(36):
    t.color(colors[i % 7])
    t.forward(350)  
    t.left(170)
    


turtle.done()
import turtle as t

t.bgcolor("black")
t.speed(0)

colors = ["red", "yellow", "blue", "green", "purple"]

for i in range(201):
    t.color(colors[i % len(colors)])
    t.forward(i * 1.1)
    t.left(71)

    
t.done()import turtle as t

t.bgcolor("black")
t.speed(0)

colors = ["red", "yellow", "blue", "teal", "cyan", "magenta"]

for i in range(200):
    t.color(colors[i % len(colors)])   # 색상 반복
    t.forward(i * 2)                   # 점점 길어지는 선
    t.right(144)                   # 별 모양 각도 (360 / 5 * 2)
    t.pensize(2)                       # 선 두께




t.hideturtle()
t.done()import turtle as t

t. bgcolor ("black")
t. color("pink")
t. speed(0) # 1(가장 느림)~10(빠름)
for i in range (200):
    t. pensize (i/50)
    t. forward (i)
    t. left (65)
t. color("teal")
t. setheading (270)

for i in range(50):
    t. pensize (25 - i/2)
    t. forward (i/4)


t.done()import turtle as t
import random

t.bgcolor("cornsilk")
t.colormode(255)
t.speed(0)
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)

num_dots = 100

for i in range(1,num_dots + 1):
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,255)
    t.dot(20, (r, g, b))
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


t.done()
import turtle
import random

# 기본 설정
turtle.bgcolor("black")
turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.shape("turtle")

# 스탬프를 찍는 함수 정의
def draw_turtle(size):
    for _ in range(12):
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        t.color(r,g,b)
        t.stamp()
        t.forward(size)
        t.right(30)

t.turtlesize(2)  # 거북이 도장 크기 키우기

t.penup()
t.goto(-60, 230) # (-60, 230)로 좌표로 이동해서 첫번째 원형 그리기
t.pendown()
draw_turtle(110)

t.penup()
t.goto(-50, 180)  # (-50, 180)로 좌표로 이동해서 두번째 원형 그리기
t.pendown()
draw_turtle(80)

t.turtlesize(1) # 거북이 도장 사이즈 줄이기

t.penup()
t.goto(-30, 100)  # (-30, 100)로 좌표로 이동해서 세번째 원형 그리기
t.pendown()
draw_turtle(40)

turtle.done() # 완료 후 창유지
# 무작위로 터틀 15마리를 생성합니다.

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
# 무작위로 터틀 15마리를 생성합니다.

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
try:
    # 파일 열기
    with open("log.txt", "r") as file:
        text = file.read() 
except FileNotFoundError as e:
    print("파일 찾기 실패", e)
    # 단어 수 세기
    words = text.split()

    # 글자 수 세기
    letters = 0
    for i in text:
        if i.isalpha(): # 알파벳만 카운트
            letters += 1

    # 단어 빈도 계산
    target = input("찾고 싶은 단어를 입력하세요.").lower()
    count = 0
    for j in text:
        if j.lower() == target:
            count += 1

    # 결과 출력
    print("파일 내용 분석")
    print("단어 갯수", len(words))
    print("글자 수", letters)
    print(f"'{target}' 등장 횟수: ", count)import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(0)
t.hideturtle() # 터틀 숨기기

for i in range(100):
    t.color(i/100,i/100,0)
    for j in range(0,4):
        t.forward(150)
        t.right(90)
    t.right(3.6)
   
turtle.exitonclick()n = int(input("Enter a Number :"))
count = 0
for i in range(1, n+1):
    count += 1
    print(f"1부터 {n}까지 합은? " ,count)import turtle

# 화면 설정
scr = turtle.Screen()
scr.title("Straight Line Art")
turtle.bgcolor("aliceblue")  # 캔버스 색상

# 터틀 설정
t = turtle.Turtle()
t.pensize(10)  # 선 굵기 설정
t.pencolor("teal")
t.speed(3)    # 그리기 속도
t.hideturtle()


t.penup()              
t.goto(-220, -200)    
t.pendown()    
t.goto(-220,200)        
t.goto(-120, 200)    
t.penup()
t.goto(-220, 30)
t.pendown()
t.goto(-120,30)
t.penup()
t.goto(-10,-10)
t.pendown()
t.circle(50)
t.penup()
t.goto(-10,20)
t.write("Rex", align="center", font=("Arial",15,"bold"))
t.penup()
t.goto(110,-10)
t.pendown()
t.circle(50)
t.penup()  
t.goto(110,20)  
t.write("fool", align="center", font=("Arial",15,"bold"))  
t.penup()
t.goto(220, -200)    
t.pendown()           
t.goto(220, 200)
turtle.done()��ǻ�� �̸�: BOOK-EU0O54PESN
IP �ּ�: 192.168.219.208
���� IP �ּ�: 58.29.221.86
MAC �ּ�: a0:b3:39:06:92:3f
import turtle
import random

turtle.bgcolor("aliceblue")
t = turtle.Turtle()
t.pensize(1)
t.speed(10)  
t.pencolor("teal")

# === fill_color 함수에 radius 추가 ===

def rand_color():
    colors = ["honeydew","cyan","deepskyblue","seagreen","palegreen","powderblue","lightgreen"]
    return random.choice(colors)


def fill_color(radius):
    t.fillcolor(rand_color())
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# 초기 시작
t.penup()
t.goto(0, -230)
t.pendown()
t.circle(250)

# 선 연결: penup 대신 pendown으로 이동
t.goto(250, 0)  
t.goto(-250, 0)
t.goto(0, 270)
t.goto(0, -230)
t.goto(0, -170)  
fill_color(180)  # radius 180으로 호출
t.goto(0, 170) 
fill_color(25)
t.goto(110, 120)
fill_color(25)
t.goto(170, -20)
fill_color(25) # 랜덤 색상
t.goto(-170, -20)
fill_color(25)
t.goto(120, -130)
fill_color(25)

# 텍스트와 선 연결
t.goto(120, -110)  # 선으로 이동
t.write("230", align="center")
t.goto(105, -90)
t.goto(-125, 125)  
t.goto(-125,0)
t.goto(-100, -85)
t.goto(100, 125)
t.goto(-130, 120)
t.fillcolor("gold")
t.begin_fill()
t.circle(20)
t.end_fill()
t.goto(-130, 130)
t.write("100", align="center")
t.goto(0, 80)
fill_color(20)
t.goto(-20, 20)
t.fillcolor("lightseagreen")
t.begin_fill()
for _ in range(5):
    t.forward(40)
    t.right(72)  # 오각형
t.end_fill()
t.goto(0, -10)
t.write("443", align="center")
t.goto(-140, -80)
t.fillcolor("lightseagreen")
t.begin_fill()
for _ in range(4):
    t.forward(50)
    t.right(90)  # 사각형
t.end_fill()
t.goto(-110, -110)
t.write("80", align="center")

turtle.exitonclick()import turtle

scr = turtle.Screen()
scr.bgcolor("wheat")
scr.title("My turtle art")  # 스크린 색상과 제목 지정

t = turtle.Turtle()
t.pensize(1)
t.speed(0)
t.hideturtle()
colors = ["red","orange","yellow","teal","skyblue","green","purple","brown"] # 그림에 사용할 색상

t.penup()
t.goto(0,30)
t.pendown()

# 8개 큰 원(45도 회전)과 각 원에 8개 원이 겹치면서 아름다운 패턴을 만들어 냅니다. 

for i in range(8):
    
    t.color(colors[i]) # 색상을 0~7번까지 번갈아가며 사용합니다.
    t.circle(90)
    t.left(45)
    
    for i in range(8):
    
        t.color(colors[7-i]) # 색상을 7~0번까지 번갈아가며 사용합니다.
        t.circle(90)
        t.right(20)

        
turtle.done()# 은행 거래 기록 프로그램

from datetime import datetime

def open_account(): #계좌 개설 함수
    print("새로운 계좌를 개설합니다")

def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 반환

def withdraw(balance, money): # 출금 처리 함수
    if balance >= money:
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance # 기존 잔액 반환

  
#계좌 개설
open_account()
while True:
    password = input("비밀번호를 설정하세요(4자리 숫자만) : ")
    if len(password) == 4 and password.isdigit():
        break

    print("4자리 숫자만 입력하세요.")

records = [] # 입출금 기록용, 빈 리스트 선언

try:
    balance = 0
    # 입금 
    my_money = int(input("입금할 금액 입력(숫자만) : "))
    balance = deposit(balance, my_money)
    records.append((f"[입금] +{my_money}원 | {datetime.now()} | 잔액 {balance}")) # 입금 기록 리스트 추가

    # 계좌 비밀 번호 확인
    check = input("비밀 번호를 입력하세요 : ")
    if check != password:
        print("비밀번호 오류. 출금 불가.")
    else:
        # 출금
        your_money = int(input("출금할 금액 입력(숫자만) : "))
        balance = withdraw(balance, your_money)
        records.append((f"[출금] -{your_money}원 | {datetime.now()} | 잔액 {balance}")) # 출금 기록 리스트 추가

    check = input("비밀 번호를 입력하세요 : ")
    if check != password:
        print("비밀번호 오류. 출금 불가.")
    else:
        # 출금
        your_money = int(input("출금할 금액 입력(숫자만) : "))
        balance = withdraw(balance, your_money)
        records.append((f"[출금] -{your_money}원 | {datetime.now()} | 잔액 {balance}")) # 출금 기록 리스트 추가

except ValueError as e:
    print("숫자만 입력하세요 : ", e)

# 거래내역 출력
print("\n=======거래내역======")
for item in records:
    print(item)

# 입출금 거래 내역과 시간 파일에 기록

with open("bank_records.txt", "a", encoding="utf-8") as f:
    f.write("\n" + "="*30 + "\n")
    f.write(f"은행 거래 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*30 + "\n")
    for item in records:
        f.write(item + "\n")
    f.write(f"최종 잔액: {balance}원\n")
    f.write("="*30 + "\n")
RIFF�u< WAVEfmt      ��   �      datahX<  �(9 `9 �p9 P�9 �l9 @Q9   9  D9 @9 �19 �f8 �"9 ��8 �
9  �7  ˸  ��  � @�8 @�8 ��8 �9  H8  <8  �5  f� �� �x�  :�  �  J7  �7   �  �  �7 �a�  �7  � ��� �� �#�  �� ��� �� �Ǹ @F� ���  A�  �� ��� �� �,� ��  x�  /� �9� @ո ���  � �from datetime import datetime


attempts = 3
while attempts > 0:
    attempts -= 1
    username = input("Enter your username : ")
    print("Security Check Starting!")

    if username == "safeuser":
        print("Username matched whitelist")
    
        with open("C:/python/security.log", "a") as f:
            f.write(f"{datetime.now()} | LOGIN | username='{username}' | attempts left={attempts}\n")
        break
    else:
        print("Warning: Username is risky!")
      
if attempts == 0:
    print("Game over!")
    with open("C:/python/security.log", "a") as f:
                f.write(f"{datetime.now()} | LOGIN FAILED | username='{username}' | attempts left={attempts}\n")2025-09-23 20:57:51.827486 | PRIME | n=15 | result=No
2025-09-23 20:57:55.536451 | PRIME | n=1 | result= 소수가 아닙니다.
2025-09-23 20:59:49.040068 | PRIME | n=13 | result=Yes
2025-09-23 21:06:50.012120 | PRIME | n=13 | result=Yes
2025-09-23 21:07:00.250321 | PRIME | n=15 | result=No
2025-09-23 21:07:04.779290 | PRIME | n=1 | result= 소수가 아닙니다.
2025-09-23 21:07:41.451664 | PRIME | n=13 | result=Yes
2025-09-23 21:07:55.344076 | ERROR | Invalid input
2025-09-23 21:08:02.767665 | PRIME | n=1 | result=No.
2025-09-23 21:08:51.370122 | PRIME | n=13 | result=Yes
2025-09-23 21:10:14.586328 | PRIME | n=13 | result=Yes
2025-09-23 21:10:18.873334 | PRIME | n=15 | result=No
2025-09-23 21:10:23.376910 | PRIME | n=1 | result=No
import sys

# 라면 끓이기 시작
print("라면 끓이기를 시작합니다!")
choice = input("라면을 끓이겠습니까? (네/아니오): ")
if choice == "아니오":
    print("안녕히가세요!")
    sys.exit()  # 프로그램 종료

# 물의 양 입력
while True:
    try:
        water = int(input("물의 양은? (숫자만 입력): "))
        if water <= 200:
            print("물의 양은 200을 넘어야 해요!")
            continue
        elif water > 1000:
            print("물이 너무 많습니다. 다시 입력하세요")
            continue
        break
    except ValueError:
        print("숫자만 입력하랬죠!")

# 물 양에 따른 처리
if water >= 450 and water <= 600:
    print("라면을 끓입니다!")
elif water < 450:
    print("물의 양이 너무 적습니다. 짜게 될 거예요!")
else:
    print("물이 너무 많습니다. 싱거울 거예요!")

# 토핑 선택
topping = input("토핑을 고르세요 (계란/파/없음): ")
if topping == "계란" or topping == "파":
    print(f"{topping}을 추가해 더 맛있게!")
else:
    print("토핑 없이 깔끔하게!")

# 라면 끓이기 과정
print("물을 끓이는 중...")
print("스프와 면을 넣고 3분 끓입니다.")
if topping == "계란":
    print("계란을 넣고 1분 더 끓여 반숙 완성!")
elif topping == "파":
    print("파를 넣고 30초 더 끓여 향긋하게!")
print("완성! 맛있게 드세요!")2025-09-19 21:05:26.813699 | LOGIN FAILED | username='33' | attempts left=0
2025-09-19 21:06:06.777059 | LOGIN | username='safeuser' | attempts left=1
2025-09-19 21:09:48.857061 | LOGIN | username='safeuser' | attempts left=1
2025-09-19 21:10:11.826152 | LOGIN FAILED | username='2sdd' | attempts left=0
2025-09-19 21:10:24.860413 | LOGIN | username='safeuser' | attempts left=2
2025-09-19 21:22:11.696085 | LOGIN FAILED | username='234' | attempts left=0
2025-09-19 21:31:50.428639 | LOGIN FAILED | username='& C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe c:/python/Untitled.py' | attempts left=0
import turtle

t = turtle.Turtle()
t.shape("turtle")

for _ in range(12):
    t.stamp()
    t.forward(50)
    t.right(30)

turtle.done()

import turtle
def draw_circle(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_square(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

def draw_triangle(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()

def draw_star(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(50)
        t.left(144)
    t.end_fill()

turtle.bgcolor("aliceblue")
t = turtle.Turtle()
t.hideturtle()
t.pencolor("black")
t.pensize(3)

draw_circle(-130,-70,"gold")
draw_circle(130,-70,"cyan")
draw_square(105,120,"orange")
draw_square(-155,120,"crimson")
draw_triangle(105,170,"deepskyblue")
draw_triangle(-155,170,"plum")
draw_star(-150,-150,"yellow")
draw_star(110,-150,"coral")
turtle.done()import turtle
import random
t = turtle.Turtle()
turtle.bgcolor("aliceblue")
t.hideturtle()
t.pencolor("black")
t.speed(1)
t.pensize(3)

# === 도형 그리기 함수 ===
def draw_circle(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def draw_square(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()

def draw_triangle(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(20)
        t.left(120)
    t.end_fill()

def draw_pentagon(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(20)
        t.left(72)
    t.end_fill()


colors = ["gold", "cyan", "orange", "crimson", "deepskyblue", "plum", "lime", "violet", "pink", "coral"]
shapes = [draw_circle, draw_square, draw_triangle, draw_pentagon]


for _ in range(20):
    shape = random.choice(shapes)
    color = random.choice(colors)
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    shape(x, y, color)  


turtle.done()import tkinter as tk
from time import strftime

# 윈도우 생성
root = tk.Tk()
root.title("나만의 디지털 시계")

# 창 크기 확장 (너비 500, 높이 250)
root.geometry("400x150")

# 날짜와 시간 표시 함수
def time():
    current_time = strftime('%H:%M:%S %p')       # 시:분:초 AM/PM
    current_date = strftime('%Y-%m-%d (%a)')     # 연-월-일 (요일)
    
    # 시간 라벨 갱신
    label_time.config(text=current_time)
    # 날짜 라벨 갱신
    label_date.config(text=current_date)
    
    # 1초마다 자동으로 다시 실행
    label_time.after(1000, time)

# 날짜 라벨 (작게 위쪽)
label_date = tk.Label(
    root,
    font=('calibri', 20, 'bold'),
    background='purple',
    foreground='white'
)
label_date.pack(pady=10)  # 여백

# 시간 라벨 (크게 가운데)
label_time = tk.Label(
    root,
    font=('calibri', 50, 'bold'),
    background='purple',
    foreground='white'
)
label_time.pack(anchor='center')

# 함수 실행
time()

# 창 유지
root.mainloop()import turtle
turtle.bgcolor("lightyellow")
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.pencolor("teal")


for i in range(80):
    t.forward(i*5)
    t.left(90)


turtle.done()import sys
sys.stdout.write("Hello, Ray?")

import sys
sys.stdout.write("Hello, Ray?")

import sys
sys.stdout.write("Hello, Ray?")

import sys
sys.stdout.write("Hello, Ray?")

import sys
sys.stdout.write("Hello, Ray?")

import sys
sys.stdout.write("Hello, Ray?")

import sys
sys.stdout.write("Hello, Ray?")from datetime import datetime
while True:
    try: 
        num = int(input("숫자를 맞춰봐 : "))
        if num >= 6:
            print("Correct!")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} |CORRECT| = {num}\n")
                break
        elif num >= 4:
            print("Good! Try again")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} |GOOD| = {num}\n")
    
        else:
            print("Try again")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} |TRY AGAIN| = {num}\n")

    except ValueError as e:
        print("Enter a number", e)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} |ERROR| = {e}\n")import turtle
turtle.bgcolor("lightyellow")
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.pencolor("teal")


for i in range(80):
    t.forward(i*5)
    t.left(90)

t.penup()
t.goto(300,300)

turtle.done()