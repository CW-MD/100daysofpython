import turtle
import pandas
screen = turtle.Screen()
#screen.setup(width=720, height=500)
screen.title('50 States Guessing Game')
image = 'day26/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
game_running = True
guessed_states = []
state_raw = pandas.read_csv('day26/50_states.csv')
state_list = state_raw.state.to_list()


while len(guessed_states) < 50:
    user_input = screen.textinput(f'{len(guessed_states)}/50', "Name another state").title()

    if user_input in state_list:
        cur_state = state_raw[state_raw.state == user_input]
        print(cur_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.pu()
        guessed_states.append(user_input)
        writer.goto(int(state_raw[state_raw.state == user_input].x), int(state_raw[state_raw.state == user_input].y))
        writer.pd()
        writer.write(user_input)

turtle.mainloop()


# screen.exitonclick()

#def get_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_click_coor)
