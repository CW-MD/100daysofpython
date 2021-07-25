from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color('white')
        self.goto(0,200)
        self.pd()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write(f'{self.left_score} | {self.right_score}')

    def update_score(self, side):
        if(side == 'left'):
            self.left_score += 1
        if(side == 'right'):
            self.right_score +=1
        self.clear()
        self.write(f'{self.left_score} | {self.right_score}')

    
