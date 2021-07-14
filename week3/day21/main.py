from time import sleep
from snake import Snake
from turtle import Screen, Turtle, color

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snek')
screen.tracer(0)

game_on = True

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_on:
    screen.update()
    sleep(0.08)
    
    snake.move()
screen.exitonclick()