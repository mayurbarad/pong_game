from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=left_paddle.go_up,key='w')
screen.onkey(fun=left_paddle.go_down,key='s')
screen.onkey(fun=right_paddle.go_up,key='Up')
screen.onkey(fun=right_paddle.go_down,key='Down')


game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when ball goes out of right screen
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect when ball goes out of left screen
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()