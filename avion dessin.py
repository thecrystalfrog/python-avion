import turtle
sc=turtle.Screen()
sc.bgcolor('black')
turtle.pensize(6)
turtle.goto(0,-250)
turtle.pencolor('green')
turtle.lt(87)
turtle.fd(20)
turtle.rt(87)
turtle.fd(70)
turtle.lt(90)
turtle.fd(40)
turtle.lt(60)
turtle.fd(10)
turtle.lt(120)
turtle.fd(45)
turtle.bk(45)
turtle.rt(120)
turtle.fd(60)

turtle.lt(120)
turtle.fd(50)


turtle.lt(90)
turtle.fd(50)
turtle.lt(180)
turtle.fd(50)
turtle.rt(83)
turtle.fd(90)
turtle.lt(167)
turtle.fd(90)

turtle.penup()
turtle.goto(0,-250)
turtle.rt(85)
turtle.pendown()

turtle.rt(87)
turtle.fd(20)
turtle.lt(87)
turtle.fd(70)
turtle.rt(90)
turtle.fd(40)

turtle.rt(60)
turtle.fd(10)
turtle.rt(120)
turtle.fd(45)
turtle.bk(45)
turtle.lt(120)
turtle.fd(60)
turtle.rt(120)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)
turtle.bk(50)            #jusqu'ici, c'est la queue

turtle.penup()
turtle.rt(95)
turtle.fd(100)

turtle.rt(170)
turtle.fd(100)
turtle.pendown()         #position pour faire la partie droite

turtle.pencolor('white')
turtle.rt(189)
turtle.fd(200)           #morceau du fuselage

turtle.pencolor('blue')
turtle.rt(80)
turtle.fd(220)           #aile droite

turtle.lt(88)
turtle.fd(50)
turtle.lt(84)
turtle.fd(200)

turtle.pencolor('white')
turtle.lt(80)
turtle.fd(85)

turtle.bk(25)
turtle.lt(107)

turtle.pencolor('blue')
turtle.fd(215)
turtle.bk(110)
turtle.rt(85)
turtle.fd(20)
turtle.bk(20)           #aile droite

turtle.penup()
turtle.goto(0,-250)
turtle.rt(3)
turtle.setheading(92)
turtle.fd(20)
turtle.lt(87)
turtle.fd(70)
turtle.rt(90)
turtle.fd(40)
turtle.rt(60)
turtle.fd(10)
turtle.rt(120)
turtle.fd(45)
turtle.bk(45)
turtle.lt(120)
turtle.fd(60)
turtle.rt(120)
turtle.fd(50)
turtle.pendown()
turtle.pencolor('white')
turtle.lt(185)
turtle.fd(200)

turtle.pencolor('blue')   #aile gauche
turtle.lt(80)
turtle.fd(220)
turtle.rt(88)
turtle.fd(50)
turtle.rt(84)
turtle.fd(200)
turtle.rt(80)

turtle.pencolor('white')
turtle.fd(85)
turtle.bk(25)            #morceau du fuselage

turtle.pencolor('blue')
turtle.rt(107)
turtle.fd(215)
turtle.bk(110)
turtle.lt(85)
turtle.fd(20)
turtle.bk(20)
turtle.lt(96)
turtle.fd(100)           #aile gauche

turtle.penup()
turtle.goto(0,200)
turtle.setheading(0)
turtle.pendown()
turtle.pencolor('white')
turtle.fd(30)
turtle.rt(85)
turtle.fd(125)
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.setheading(180)
turtle.fd(30)
turtle.lt(86)
turtle.fd(125)
turtle.penup()
turtle.goto(30,200)
turtle.pendown()
turtle.lt(180)
turtle.circle(30,180)







turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
turtle.done()
