import turtle as t

# draw Taegeuk

t.setup(600, 400)
t.bgcolor("black")
t.title("Taegeuk")

def Taegeuk(radius=80):
    t.up()
    t.goto(radius, 0) 
    t.down()
    t.seth(90)

    t.color("#EE2132")              
    t.begin_fill()
    t.circle(radius, 180)          
    t.end_fill()

    t.color("#0C62D2")              
    t.begin_fill()
    t.circle(radius, 180)           
    t.end_fill()

    t.seth(90)
    t.color("#0C62D2")             
    t.begin_fill()
    t.circle(radius/2, 180) 
    t.end_fill()

    t.seth(180)
    t.fd(radius)
    t.seth(270)
    t.color("#EE2132")              
    t.begin_fill()
    t.circle(radius/2, 180) 
    t.end_fill()
    t.ht()

Taegeuk()

t.done()
