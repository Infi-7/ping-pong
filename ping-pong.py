# Imports 
import turtle


# Basic Screen
win = turtle.Screen()
win.title("Ping-Pong")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

score_a = 0
score_b = 0

# Player Bars
# Pad A
pad_a = turtle.Turtle()
pad_a.shape("square")
pad_a.speed(0)
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.color("white")
pad_a.penup()
pad_a.goto(-350,0)

# Pad B
pad_b = turtle.Turtle()
pad_b.shape("square")
pad_b.speed(0)
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.color("white")
pad_b.penup()
pad_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

# Score Card
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"normal"))


# Working
def move_pad_a_up():
    y = pad_a.ycor()
    y += 20
    if y > 260:
        pad_a.sety(260)
    else:
        pad_a.sety(y)    


def move_pad_a_down():
    y = pad_a.ycor()
    y -= 20
    if y < -260:
        pad_a.sety(-260)
    else:
        pad_a.sety(y)

def move_pad_b_up():
    y = pad_b.ycor()
    y += 20
    if y > 260:
        pad_b.sety(260)
    else:
        pad_b.sety(y)

def move_pad_b_down():
    y = pad_b.ycor()
    y -= 20
    if y < -260:
        pad_b.sety(-260)
    else:
        pad_b.sety(y)

# Keyboard Listener
win.listen()
win.onkeypress(move_pad_a_up,"w")
win.onkeypress(move_pad_a_down,"s")
win.onkeypress(move_pad_b_up,"Up")
win.onkeypress(move_pad_b_down,"Down")

# Main Loop
while True:
    win.update()

# Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # hits y-cord and reverses

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # hits y-cord and reverses

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

# Hitting Logic

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1