from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

#screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#creating all of the objects
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
sb = ScoreBoard()

screen.listen()
#allow paddles to go up and down
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

#calls the function from the paddle class in order for the paddle to move up and down
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #bounce off the wall(change the y cor)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #bounce ball off the paddle and change the direction of the x cor
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed -= 0.005
    #if the ball touches the end of the screen call the reset ball function to return the ball back to the center
    #also reset the paddles to the original position
    if ball.xcor() > 400:
        ball.reset_ball()
        l_paddle.reset_position(-350,0)
        r_paddle.reset_position(350,0)
        sb.l_point()
        ball.move_speed = 0.1

    if ball.xcor() < -400:
        ball.reset_ball()
        l_paddle.reset_position(-350, 0)
        r_paddle.reset_position(350, 0)
        sb.r_point()
        ball.move_speed = 0.1

screen.exitonclick()