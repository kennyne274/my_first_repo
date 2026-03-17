import turtle as t

# Drawing  cute Lion
# Actually, This is my python teather's project.
# I listened to her lecture and wrote this code.

t.setup(680, 800)
t.bgcolor("lightcyan")
t.pensize(5)
t.speed(9)
t.color("black", "#eea033")

# Lion's body
t.up()
t.goto(-90, 20)
t.down()
t.begin_fill()

# left arm
t.seth(220)
t.circle(80, 100)

# both legs
t.seth(270)
t.forward(100)
t.circle(35, 180)
t.forward(20)
t.right(90)
t.fd(40)
t.right(90)
t.fd(20)
t.circle(35, 180)
t.fd(100)

# right arm
t.seth(40)
t.circle(80, 100)
t.goto(-90, 20)
t.end_fill()

# a dividing line between the arms and the body
t.penup()
t.goto(-90, -30)
t.pendown()
t.goto(-90, -100)
t.penup()
t.goto(90, -30)
t.pendown()
t.goto(90, -100)

# a pattern on the chest
t.color("white", "white")
t.up()
t.goto(40, -40)
t.down()
t.begin_fill()
t.goto(20, -60)
t.goto(0, -40)
t.goto(-20, -60)
t.goto(-40, -40)
t.seth(240)
t.circle(47, 240)
t.end_fill()

# ear
t.color("black", "#eea033")
t.up()
t.goto(-70, 210) # left ear
t.down()
t.begin_fill()
t.seth(120)
t.circle(30, 210)
t.end_fill()
t.up()
t.goto(70, 210) # right  ear
t.down()
t.begin_fill()
t.seth(60)
t.circle(-30, 210)
t.end_fill()

# face
t.up()
t.goto(0, 230)
t.down()
t.begin_fill()
t.seth(180)
t.circle(130)
t.end_fill()

# Eyebrows
t.pensize(10)
t.up()
t.goto(-80, 130)
t.down()
t.goto(-30, 130)
t.up()
t.goto(80, 130)
t.down()
t.goto(30, 130)

# eyes
t.up()
t.goto(-55, 110)
t.dot(15)

t.goto(55, 110)
t.dot(15)

# nose
t.pensize(5)
t.color("black", "white")
t.up()
t.goto(-10, 80)
t.down()
t.begin_fill()
t.seth(155)
t.circle(18, 240)
t.circle(25, 25)
t.right(116)
t.circle(25, 25)
t.circle(18, 240)
t.goto(0, 80)
t.dot(20)
t.end_fill()

t.ht()
t.done()
