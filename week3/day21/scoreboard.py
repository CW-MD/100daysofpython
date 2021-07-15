from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.goto(-10,280)
        

    def update(self):
        self.clear()
        self.write(font=('ariel',12,'bold'),arg= f'Score: {self.score}')

    def game_over(self):
        self.pu()
        self.goto(-125,0)
        self.write(font=('ariel', 32, 'bold'),arg='GAME OVER')