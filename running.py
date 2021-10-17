# Created By Raghav

import datetime
import turtle

wn = turtle.Screen()
wn.setup(width=1100, height=1100)
wn.title('Analog Clock')
wn.setworldcoordinates(-1100, -1100, 1100, 1100)
wn.bgcolor('black')
wn.tracer(0,0)

turtle.penup()
turtle.hideturtle()
turtle.goto(0,-820)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(820)
turtle.end_fill()



class clock:
    def __init__(self, hour, minute, second):
        self.hour, self.minute, self.second = hour, minute, second
        self.face = turtle.Turtle()
        self.hand = turtle.Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()

    def draw(self):
        self.draw_face()
        self.clockhands()
        self.draw_hands()

    def draw_face(self):
        self.face.penup()
        self.face.goto(0, -780)
        self.face.pen('white')
        self.face.fillcolor('#7ad0e4')
        self.face.begin_fill()
        self.face.circle(700)
        self.face.end_fill()
        self.face.goto(0, -780)
        self.face.fillcolor('#cfebef')
        self.face.begin_fill()
        self.face.circle(780)
        self.face.end_fill()
        self.face.goto(0, 0)
        self.face.setheading(90)

    def clockhands(self):
        for i in range(12):
            self.face.pensize(3)
            self.face.pencolor('black')
            self.face.penup()
            self.face.fd(780)
            self.face.pendown()
            self.face.bk(100)
            self.face.penup()
            self.face.bk(680)
            self.face.rt(6)
            self.face.pendown()
            self.face.pencolor('green')
            self.face.penup()
            self.face.fd(780)
            self.face.pendown()
            self.face.bk(50)
            self.face.penup()
            self.face.bk(730)
            self.face.rt(6)
            self.face.pendown()
            self.face.penup()
            self.face.fd(780)
            self.face.pendown()
            self.face.bk(50)
            self.face.penup()
            self.face.bk(730)
            self.face.rt(6)
            self.face.pendown()
            self.face.penup()
            self.face.fd(780)
            self.face.pendown()
            self.face.bk(50)
            self.face.penup()
            self.face.bk(730)
            self.face.rt(6)
            self.face.pendown()
            self.face.penup()
            self.face.fd(780)
            self.face.pendown()
            self.face.bk(50)
            self.face.penup()
            self.face.bk(730)
            self.face.rt(6)
            self.face.pendown()

    def draw_hand(self):
        self.hand.clear()
        self.hand.penup()
        self.hand.goto(0, 0)
        self.hand.seth(90 - self.hour % 12 * 360 // 12)
        hourdeg = (12 - self.hour) * 30 + 90
        hourdeg = hourdeg - (self.minute / 2)
        self.hand.setheading(hourdeg)
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(6)
        self.hand.fd(250)

        self.hand.penup()
        self.hand.goto(0, 0)
        minutedeg = (60 - self.minute) * 6 + 90
        self.hand.setheading(minutedeg)
        self.hand.down()
        self.hand.color('blue')
        self.hand.pensize(4)
        self.hand.fd(500)

        self.hand.penup()
        self.hand.color('red')
        self.hand.goto(0, 0)
        self.hand.dot(5)
        seconddeg = (60 - self.second) * 6 + 90
        self.hand.setheading(seconddeg)
        self.hand.down()
        self.hand.pensize(2)
        self.hand.fd(400)

def animate():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second = d.hour, d.minute, d.second
    c.draw_hand()
    wn.update()
    wn.ontimer(animate, 1000)


d = datetime.datetime.now()
c = clock(d.hour, d.minute, d.second)
c.draw_face()
c.clockhands()
def number12():
    pen = turtle.Turtle()
    # number 1
    pen.penup()
    pen.hideturtle()
    pen.goto(300, 475)
    pen.write("1", align="center", font=("Algerian", 50, "bold"))

    # number 2
    pen.penup()
    pen.hideturtle()
    pen.goto(545, 240)
    pen.write("2", align="center", font=("Algerian", 50, "bold"))

    # number 3
    pen.penup()
    pen.hideturtle()
    pen.goto(635, -62)
    pen.write("3", align="center", font=("Algerian", 50, "bold"))

    # number 4
    pen.penup()
    pen.hideturtle()
    pen.goto(540, -375)
    pen.write("4", align="center", font=("Algerian", 50, "bold"))

    # number 5
    pen.penup()
    pen.hideturtle()
    pen.goto(310, -590)
    pen.write("5", align="center", font=("Algerian", 50, "bold"))

    # number 6
    pen.penup()
    pen.hideturtle()
    pen.goto(0, -675)
    pen.write("6", align="center", font=("Algerian", 50, "bold"))

    # number 7
    pen.penup()
    pen.hideturtle()
    pen.goto(-310, -590)
    pen.write("7", align="center", font=("Algerian", 50, "bold"))

    # number 8
    pen.penup()
    pen.hideturtle()
    pen.goto(-540, -375)
    pen.write("8", align="center", font=("Algerian", 50, "bold"))

    # number 9
    pen.penup()
    pen.hideturtle()
    pen.goto(-635, -62)
    pen.write("9", align="center", font=("Algerian", 50, "bold"))

    # number 10
    pen.penup()
    pen.hideturtle()
    pen.goto(-515, 240)
    pen.write("10", align="center", font=("Algerian", 50, "bold"))

    # number 11
    pen.penup()
    pen.hideturtle()
    pen.goto(-300, 475)
    pen.write("11", align="center", font=("Algerian", 50, "bold"))

    # number 12
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 565)
    pen.write("12", align="center", font=("Algerian", 50, "bold"))

number12()
turtle.goto(0,-50)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
wn.update()
animate()

turtle.done()


