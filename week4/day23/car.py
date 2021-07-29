from turtle import Turtle
from random import choice
COLORS = ['orange','yellow','green','blue','purple','red']

CAR_SPEED = 5
CAR_SPEED_INC = 10

class Car(Turtle):
    def __init__(self,y):
        super().__init__()
        self.shape('square')
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.speed(1)
        self.goto(300, y)


    def move_car(self):
        self.goto(self.xcor() - 10, self.ycor())