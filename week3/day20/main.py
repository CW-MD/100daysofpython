from turtle import Turtle, Screen, shape, xcor
import random
screen = Screen()
screen.setup(height=400,width=500)

colors = ['red', 'orange','yellow', 'green', 'blue', 'purple']

#When a turtle reaches the win_goal, race ends (turt.xPos >= 200)

turtle_list = []
win_goal = 200
won=False
y_offset = -100



for num in range(0,6):
    turt = Turtle(shape='turtle')
    turt.pu()
    turt.goto(x=-200,y=y_offset)
    turt.color(colors[num])
    turt.speed('slowest')
    y_offset += 40
    turtle_list.append(turt)


prompt = screen.textinput(title='Turtle Gambling Simulator', prompt='Which color turtle do you think will win?')

def race(turtle):
    global won
    turtle.setx(turtle.xcor() +random.randint(1,20) )
    if turtle.xcor() >= 200:
        print(f'{turtle.color()} wins!')
        won= True
        


while won == False:
    for turtle in turtle_list:
        race(turtle)
    





screen.exitonclick()