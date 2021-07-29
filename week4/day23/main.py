from turtle import Screen
from car import Car
from time import sleep
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
game_running = True
positions = [(250,200),(250,190),(250,180),(250,170),(250,160),(250,150),(250,140),(250,130),(250,120),(250,110),(250,100)]


while game_running:
    #print(positions[0][1])

    x = random.randint(0,len(positions) - 1)
    print(x)
    car1 = Car(positions[x][0], positions[x][1])
    car1.move_car()
        #car = Car()
    sleep(.1)
    screen.update()
    




screen.exitonclick()
