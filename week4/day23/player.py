from turtle import Turtle

STARTING_POS = (0,-200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, shape: str, undobuffersize: int, visible: bool):
        super().__init__(shape=shape, undobuffersize=undobuffersize, visible=visible)