import turtle as t

t.bgcolor("black")
t.speed(0)

colors = ["red", "yellow", "blue", "teal", "cyan", "magenta"]

for i in range(200):
    t.color(colors[i % len(colors)])   # 색상 반복
    t.forward(i * 2)                   # 점점 길어지는 선
    t.right(144)                   # 별 모양 각도 (360 / 5 * 2)
    t.pensize(2)                       # 선 두께




t.hideturtle()
t.done()