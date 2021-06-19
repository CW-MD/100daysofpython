import os, art
clear = lambda: os.system('clear')
clear()
print(art.logo)
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


ops = {
    '+': add,
    '-':subtract,
    '*':multiply,
    '/':divide,
    }

symbols = '+ - * /'
should_continue = True

num1 = int(input('What is your first number? :'))
while(should_continue):
    print(f"Operations: {symbols}")
    cur_op = input('Please pick an operation: ')

    num2 = int(input('What is your next number? :'))


    calc_function = ops[cur_op]
    answer = calc_function(num1, num2)
    print(answer)

    repeat = input('Would you like to perform another operation?: Y / N : ').lower()
    if repeat == 'y':
        num1 = answer
    if repeat == 'n':
        should_continue = False



#MFW my current version doesnt support match-case :(
# match cur_op:
#     case "+":
#         add(num1, num2)
#     case "-":
#         subtract(num1, num2)
#     case "*":
#         multiply(num1, num2)
#     case "/":
#         divide(num1, num2)
