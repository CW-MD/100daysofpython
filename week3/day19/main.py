from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move():
    turt.forward(15)

def turn_left():
    turt.left(20)

def turn_right():
    turt.right(20)


screen.listen()
screen.onkey(key='Up', fun=move)
screen.onkey(key='Left', fun=turn_left)
screen.onkey(key='Right', fun=turn_right)

screen.exitonclick()