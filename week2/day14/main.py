#Higher - Lower Game
import random;
import data

#Print Greeting and Instructions, user input enter 'start' to start:

print('Welcome to the Higher - Lower  game!!!!!!!!!!!')

#generate 2 random numbers 0 - len(data - 1)
#If num1 == num2 : num2 = (num2 + 20) // 2
num1 = random.randint(0,len(data.data)-1)
num2 = random.randint(1,2)
if num1 == num2:
    num2 = (num2 + 20) // 2

print(len(data.data))
print(len(data.data)-1)
