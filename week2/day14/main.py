#Higher - Lower Game
import random, data

name = 'name'
followers = 'follower_count'
description = 'description'
country =  'country'
game_over = False

#Print Greeting and Instructions, user input enter 'start' to start:

print('Welcome to the Higher - Lower  game!!!!!!!!!!!')

#generate 2 random numbers 0 - len(data - 1)
#If num1 == num2 : num2 = (num2 + 20) // 2
num1 = random.randint(0,len(data.data)-1)
num2 = random.randint(0,len(data.data)-1)
if num1 == num2:
    num2 = (num2 + 20) // 2

data1 = data.data[num1]
data2 = data.data[num2]

def fetch_data(num1, num2):
    global data1, data2
    data1 = data.data[num1]
    data2 = data.data[num2]
    #print(data1, data2)

def format_strings(data1, data2):
    global prompt1, prompt2
    prompt1 = f'{data1[name]}, A {data1[description]} from {data1[country]} VS:'
    prompt2 = f"Does {data2[name]}, A {data2[description]} from {data2[country]} have 'more' or 'less' followers? "

def compare(num1, num2):
    global data1, data2
    if data1[followers] > data2[followers]:
        return 'less'
    else:
        return 'more'

expected_answer = compare(num1, num2)

prompt1 = f'{data1[name]}, A {data1[description]} from {data1[country]} VS:'
prompt2 = f"Does {data2[name]}, A {data2[description]} from {data2[country]} have 'more' or 'less' followers? "

score = 0
while not game_over:
    print(prompt1)
    user_answer = input(prompt2)
    if user_answer == expected_answer:
        score += 1
        num1 = num2
        num2 += 1
        fetch_data(num1, num2)
        format_strings(data1, data2)
        expected_answer = compare(num1, num2)
    else:
        game_over = True
        print(f'Game Over! Your final score is {score}')
