from time import sleep
from snake import Snake
from turtle import Screen, Turtle, color
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
score_board = 0
screen.bgcolor('black')
screen.title('Snek')
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
board.update()

while game_on:
    screen.update()
    sleep(0.07)
    
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        board.score +=1
        board.update()
        snake.grow()

    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        board.game_over()

    for seg in snake.segments:
        if snake.head.distance(seg) < 10 and snake.head != seg:
            board.game_over()
screen.exitonclick()