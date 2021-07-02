from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.canvheight = 800
screen.canvwidth = 800

timmy.width(5)
timmy.speed(2)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(10):
#     timmy.pd()
#     timmy.forward(20)
#     timmy.pu()
#     timmy.forward(20)


angles = 3
turn = (360/angles)
while angles < 11:
    angle_count = 0
    for _ in range(angles):
        timmy.forward(100)
        timmy.right(turn)
        angle_count += turn
        print(angle_count)
        if angle_count >= 359.99999:
            angles +=1
            turn = (360/angles)
print(timmy.color())
screen.exitonclick()
