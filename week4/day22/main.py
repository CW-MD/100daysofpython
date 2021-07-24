from turtle import Turtle, Screen, width
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pawng')
game_running = True
lPaddle = Paddle(-350,0)
rPaddle = Paddle(350,0)
ball = Ball()




screen.listen()
screen.onkey(lPaddle.move_up, 'w')
screen.onkey(lPaddle.move_down, 's')
screen.onkey(rPaddle.move_up, 'Up')
screen.onkey(rPaddle.move_down, 'Down')

while game_running:
    sleep(.01)
    ball.move()
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()

screen.exitonclick()