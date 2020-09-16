import turtle
import os

wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15


"""Functions"""
def PaddleAUp():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def PaddleADown():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def PaddleBUp():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def PaddleBDown():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)


"""Keybord Binding"""
wn.listen()
wn.onkeypress(PaddleAUp, "w")
wn.onkeypress(PaddleADown, "s")
wn.onkeypress(PaddleBUp, "Up")
wn.onkeypress(PaddleBDown, "Down")


"""game loop"""
while True:
	wn.update()

	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Morder checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1

	#paddle and ball collision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx *= -1


		



