import turtle
import pandas
screen = turtle.Screen()
screen.setup(width=720, height=500)
screen.title('50 States Guessing Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
game_running = True
guessed_states = []
state_list = pandas.read_csv('50_states.csv')

user_input = screen.textinput('Guess a State', "Name another state")

print(state_list[state_list.state == user_input])

while game_running:
    user_input = screen.textinput('Guess a State', "Name another state")
    if state_list[state_list.state == user_input]:
        guessed_states.append(state_list[state_list.state])
        turtle.pu()
        turtle.goto(state_list[state_list.state == user_input].x, state_list[state_list.state == user_input].y)
        turtle.pd()
        turtle.write(state_list[state_list.state == user_input].state)

turtle.mainloop()


# screen.exitonclick()

#def get_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_click_coor)
