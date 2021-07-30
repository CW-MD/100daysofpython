from turtle import Turtle
FONT = ('Courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f'Level: {self.level}', font=FONT)
        
    def update_score(self):
        self.level +=1 
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)



