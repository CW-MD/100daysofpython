from turtle import Turtle, Screen, shape

screen = Screen()
screen.setup(height=400,width=500)

colors = ['red', 'orange','yellow', 'green', 'blue', 'purple']

y_offset = -100
for num in range(0,6):
    turt = Turtle(shape='turtle')
    turt.pu()
    turt.goto(x=-200,y=y_offset)
    turt.color(colors[num])
    y_offset += 40
    
prompt = screen.textinput(title='Turtle Gambling Simulator', prompt='Which color turtle do you think will win?')




screen.exitonclick()