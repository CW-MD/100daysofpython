from turtle import Turtle, setheading

START_POS = [(0,0),(-20,0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        
        for pos in START_POS:
            new_seg = Turtle(shape='square')
            new_seg.color('white')
            new_seg.pu()
            new_seg.goto(pos)
            self.segments.append(new_seg)


    def move(self):
        for seg in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y) 
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0) 

    

