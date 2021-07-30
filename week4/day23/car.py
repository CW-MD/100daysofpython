from turtle import Turtle
from random import choice, randint
COLORS = ['orange','yellow','green','blue','purple','red']
CAR_START = (300, randint(-180, 260) )

CAR_SPEED_INC = 5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        #self.shape('square')
        self.car_list = []
        self.ht()
        self.car_speed = 5
        self.pu()
       # self.shapesize(stretch_wid=1, stretch_len=2)
        #self.color(choice(COLORS))
        #self.speed(1)
        #self.create_car()

    def create_car(self):
        random_choice = randint(1,5)
        if random_choice == 5:
            new_car = Turtle()
            new_car.shape('square')
            new_car.pu()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-180, 260))
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            if(car.xcor() < -300):
                self.car_list.remove(car)
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += CAR_SPEED_INC
    