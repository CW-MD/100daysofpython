from turtle import Turtle
COLORS = ['orange','yellow','green','blue','purple','red']
CAR_SPEED = 5
CAR_SPEED_INC = 10

class Car(Turtle):
    def __init__(self, *args):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        print(args)
        self.goto(args)
    def move_car(self):
        self.goto(self.xcor() - 100, self.ycor())