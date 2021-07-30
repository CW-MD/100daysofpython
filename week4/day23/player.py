from turtle import Turtle

STARTING_POS = (0,-200)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.goto(STARTING_POS)
        self.left(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_pos(self):
        self.ht()
        self.goto(STARTING_POS)
        self.st()
