from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pawng')
game_running = True
lPaddle = Paddle(-350,0)
rPaddle = Paddle(350,0)
ball = Ball()
score = Score()




screen.listen()
screen.onkey(lPaddle.move_up, 'w')
screen.onkey(lPaddle.move_down, 's')
screen.onkey(rPaddle.move_up, 'Up')
screen.onkey(rPaddle.move_down, 'Down')

while game_running:
    sleep(.04)
    ball.move()
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()
    if(rPaddle.distance(ball) < 70 and ball.xcor() > 340):
        print('hit paddle')
        ball.collide()

    if(lPaddle.distance(ball) < 70 and ball.xcor() < -340):
        ball.collide()

    if(ball.xcor() > 350):
        score.update_score('left')
        ball.ball_reset()
    if(ball.xcor() < -350):
        score.update_score('right')
        ball.ball_reset()

screen.exitonclick()