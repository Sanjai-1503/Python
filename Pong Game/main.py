import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("THE PONG GAME")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0), 5, 1)
l_paddle = Paddle((-350, 0), 5, 1)

score = Score()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.l_update()
        ball.reset_pos()

    if ball.xcor() < -380:
        score.r_update()
        ball.reset_pos()

screen.exitonclick()
