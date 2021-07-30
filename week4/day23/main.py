from turtle import Screen
from car import Car
from player import Player
from time import sleep
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
game_running = True

screen.listen()
player = Player()
score = Score()
carManager = Car()
screen.onkey(player.move_up, 'Up')


loop_counter = 0
while game_running:
    carManager.create_car()
    if player.ycor() >= 280:
        score.update_score()
        player.reset_pos()
        carManager.increase_speed()
    carManager.move_car()
    for x in carManager.car_list:
        if player.distance(x) < 20:
            print('Game Over')
            game_running = False
    print(len(carManager.car_list))
    sleep(.1)

    loop_counter+=1
    screen.update()
    
    




screen.exitonclick()
