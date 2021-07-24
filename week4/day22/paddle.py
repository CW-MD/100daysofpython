from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.pu()
        self.setup()
        
    def setup(self):
        self.goto(self.x, self.y)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)
    
    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
    