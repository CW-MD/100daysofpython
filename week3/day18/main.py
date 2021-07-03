import colorgram
from turtle import Turtle, Screen, color
import random
timmy = Turtle()
screen = Screen()
screen.canvheight = 800
screen.canvwidth = 800

screen.colormode(255)


#timmy.width(3)
timmy.speed(0)

color_list = colorgram.extract('day18/candies.jpg', 10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r,g,b)
    return new_color

directions = [0, 90, 180, 270]

#Box
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#Dashed Line
# for _ in range(10):
#     timmy.pd()
#     timmy.forward(20)
#     timmy.pu()
#     timmy.forward(20)

#Draw x sided shapes
# angles = 3
# turn = (360/angles)
# timmy.pd()

# while angles > 0:
#     angle_count = 0
#     for _ in range(angles):
#         timmy.forward(100)
#         timmy.right(turn)
#         angle_count += turn
#         print(angle_count)
#         if angle_count >= 359.99999:
#             angles +=1
#             turn = (360/angles)
#             r = random.randint(0,255)
#             g = random.randint(0,255)
#             b = random.randint(0,255)
#             timmy.color(r,g,b)

# while 1 > 0:
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)   
#     timmy.color(r,g,b)
#     timmy.forward(15)
#     timmy.setheading(random.choice(directions))

#spirograph
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(2)
#     timmy.forward(.1)
#     timmy.circle(100)

for _ in range(10):
    for _ in range(10):
        timmy.pd()
        timmy.circle(1)
        timmy.pu()
        timmy.forward(20)
        timmy.pd()
    timmy.pu()    
    timmy.sety((timmy.ycor() + 50))
    timmy.setx((timmy.xcor() - 200))



print(timmy.color())

screen.exitonclick()
