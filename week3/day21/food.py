from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(0.5,0.5)
        self.color('green')
        self.speed(10)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-260,260)
        rand_y = random.randint(-260,260)
        self.goto(rand_x,rand_y)
