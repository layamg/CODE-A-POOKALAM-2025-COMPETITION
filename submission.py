import turtle
t=turtle.Turtle()
t.speed(0)

t.penup()
turtle.colormode(255)
rads=223
colors=[[(255,150,150), (255,200,120), (255,255,180)], [(255,100,100), (255,180,80), (255,255,130)], [(255,60,60), (255,160,40), (255,240,80)], [(255,30,30), (255,140,0), (255,220,30)], [(220,0,0), (230,90,0), (230,200,0)], [(190,0,0), (200,70,0), (200,170,0)]]
for j in range(6):
    pal=colors[j]
    t.goto(0,rads)
    t.pendown()
    t.pensize(12)
    for i in range(36):
        if i%3==0:
            t.color(pal[0])
        elif i%3==1:
            t.color(pal[1])
        elif i%3==2:
            t.color(pal[2])
        t.circle(-rads,10)
    rads+=10
    t.penup()


t.penup()
t.goto(0, 218)
t.setheading(0)
t.pendown()
t.pensize(1)
t.color("white")
t.begin_fill()
t.circle(-218)
t.end_fill()


t.pensize(10)
t.color("green")
t.penup()
t.home()
t.goto(0,195)
t.pendown()
t.begin_fill()
t.circle(-195)
t.end_fill()


t.pensize(3)
t.setheading(10)
for i in range(36):
    t.penup()
    t.home()
    t.setheading(10*i)
    t.forward(202)
    t.pendown()
    t.color((255, 128, 0),(255, 255, 0))
    t.begin_fill()
    t.left(60)
    t.forward(25)
    t.left(60)
    t.forward(25)
    t.left(120)
    t.forward(25)
    t.left(60)
    t.forward(25)
    t.end_fill()


t.pensize(2)
t.color((128, 0, 0))
t.penup()
t.goto(0,190)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(-190)
t.end_fill()


t.color("white")
for j in range(12):
    t.penup()
    t.home()
    t.setheading(j*30)
    t.forward(163)
    t.right(90)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        r=20
        b=110
        if i==1:
            r=-20
            b=-110
        t.circle(r,70)
        t.left(b)
        t.circle(r, 70)
        if i==0:
            t.right(70)
        else:
            t.left(125)
    t.end_fill()


t.penup()
t.home()
t.goto(0, 150)
t.pendown()
l=13.361030158247472
for i in range(72):
    if i%3==0:
        t.color("yellow")
    elif i%3==1:
        t.color(255, 90, 0)
    elif i%3==2:
        t.color("violet")
    t.pensize(12.5)
    x=t.xcor()
    y=t.ycor()
    h=t.heading()
    for j in range(3):
        t.right(45)
        t.forward(l)
    t.penup()
    t.goto(x,y)
    t.setheading(h)
    t.circle(-150, 5)
    t.pendown()


c2=117.74361978468302
t.penup()
t.pensize(3)
t.color("red")
t.begin_fill()
t.goto(0,c2)
t.pendown()
t.setheading(0)
t.circle(-c2)
t.end_fill()
t.goto(0,100)
t.circle(-100)


a=0
t.color("green")
t.begin_fill()
for i in range(12):
    t.goto(0,100)
    a=a+30
    t.setheading(0)
    t.circle(-100,a)
    x=t.xcor()
    y=t.ycor()
    t.left(180)
    t.circle(100,30)
    t.right(120)
    t.forward(20)
    t.goto(x,y)
t.end_fill()


t.goto(0,100)
t.setheading(0)
t.circle(-100, 5)
t.color("yellow")
t.begin_fill()
a=0
for i in range(12):
    t.goto(8.72,99.62)
    a=a+30
    t.setheading(355)
    t.circle(-100,a)
    x=t.xcor()
    y=t.ycor()
    t.left(180)
    t.circle(100,30)
    t.right(120)
    t.forward(20)
    t.goto(x,y)
t.end_fill()


t.goto(0,100)
t.setheading(0)
t.circle(-100, 10)
t.color(149, 4, 169)
t.begin_fill()
for i in range(12):
    t.goto(17.36,98.48)
    a=a+30
    t.setheading(350)
    t.circle(-100,a)
    x=t.xcor()
    y=t.ycor()
    t.left(180)
    t.circle(100,30)
    t.right(120)
    t.forward(20)
    t.goto(x,y)
t.end_fill()


coord=0
t.pensize(5)
green=[(124, 179, 66),(121, 176, 65),(118, 173, 64),(115, 170, 63),(112, 167, 62),(109, 164, 61),(106, 161, 60),(103, 158, 59),(100, 155, 58),(97, 152, 57),(94, 149, 56),(91, 146, 55),(88, 143, 54),(85, 140, 53),(82, 137, 52),(79, 134, 51),(76, 131, 50),(73, 128, 49),(70, 125, 48),(67, 122, 47),(64, 119, 46),(61, 116, 45),(58, 113, 44),(55, 110, 43),(124, 179, 66)]


for i in range(25):
    t.color(green[i])
    t.penup()
    t.home()
    t.setheading(0)
    t.goto(0,coord)
    t.pendown()
    t.circle(-coord)
    coord+=4


t.penup()
t.color("black")
t.begin_fill()
t.goto(-52, 25)
t.pendown()
t.left(50)
t.circle(-38, 42)
t.circle(-38, 18)
t.right(20)
t.circle(29, 40)
t.left(35)
t.circle(-21, 15)
t.circle(-21, 75)
t.forward(21)
t.circle(5,180)
t.forward(18.5)
t.circle(-12.5,100)
t.forward(5)
t.left(15)
t.circle(-2.5, 90)
t.forward(2.5)
t.circle(-5, 80)
t.right(20)
t.forward(1.5)
t.right(15)
t.forward(2.5)
t.circle(5, 90)
t.left(25)
t.forward(17.5)
t.circle(-20, 140)
t.goto(-52, 25)
t.end_fill()


t.begin_fill()
t.setheading(230)
t.circle(38, 25)
t.forward(8.5)
t.circle(-30, 20)
t.circle(-50, 20)
t.circle(20, 10)
t.circle(5,20)
t.circle(1,150)
t.forward(9)
t.right(15)
t.circle(20, 20)
t.left(10)
t.circle(2.5, 30)
t.right(17)
t.forward(7.5)
t.circle(-30, 10)
t.circle(-1, 120)
t.forward(5)
t.circle(-30, 60)
t.forward(2.5)
t.circle(5, 5)
t.circle(15, 15)
t.forward(11)
t.circle(2, 105)
t.forward(19)
t.circle(2, 110)
t.circle(-25, 50)
t.forward(5)
t.circle(-2.5, 20)
t.forward(7.5)
t.circle(-1.5,115)
t.forward(31)
t.right(40)
t.circle(2,120)
t.forward(18)
t.left(5)
t.circle(2, 110)
t.forward(10)
t.circle(-30, 10)
t.forward(14)
t.circle(-2,110)
t.forward(10)
t.circle(50, 15)
t.circle(-2, 110)
t.forward(15)
t.circle(-60, 10)
t.forward(5)
t.circle(2, 110)
t.forward(19)
t.circle(2, 160)
t.right(60)
t.forward(10)
t.circle(-25, 30)
t.circle(-2, 130)
t.forward(7.5)
t.circle(-3.5, 70)
t.forward(7.5)
t.circle(-2.5, 80)
t.circle(0.5, 180)
t.forward(19)
t.circle(2.5, 130)
t.right(27)
t.forward(15)
t.circle(2, 35)
t.forward(30)
t.circle(-3, 60)
t.forward(2.5)
t.right(105)
t.circle(10,40)
t.left(120)
t.circle(12.5, 25)
t.right(180)
t.circle(12.5, 80)
t.left(160)
t.circle(-12.5, 80)
t.goto(48.82,-1.06)
t.goto(-52, 25)
t.end_fill()


t.goto(48.82,-1.06)
t.color("white")
t.begin_fill()
t.forward(5)
t.left(90)
t.forward(5)
t.left(90)
t.circle(16, 34)
t.goto(46.51,-5.03)
t.setheading(311)
t.circle(12.5, 80)
t.left(160)
t.circle(-12.5, 80)
t.goto(48.82,-1.06)
t.end_fill()


t.color("orange")
t.penup()
t.goto(-28.18,38.20)
t.setheading(-90)
t.pendown()
t.begin_fill()
t.color("orange","yellow")
t.pensize(5)
t.forward(50)
t.left(90)
t.forward(50)
t.goto(7.59,37.89)
t.setheading(210)
t.color("yellow")
t.circle(21, 15)   
t.right(35)              
t.circle(-29, 40)   
t.left(20)               
t.circle(38, 18) 
t.end_fill()


rad=15
t.pensize(1)
for i in range(3):
    if i==0:
        t.color("blue")
    elif i==1:
        t.color("green")
    else:
        t.color("red")
    t.penup()
    t.goto(-5.88,12.54)
    t.setheading(90)
    t.forward(rad)
    t.setheading(180)
    t.pendown()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    rad-=5


t.penup()
t.goto(33.35, 16.09)
t.pendown()
t.dot(5,"white")


t.hideturtle()
turtle.done()
