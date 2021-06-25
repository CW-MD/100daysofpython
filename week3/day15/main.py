#Coffee Machine
import data
#establishing common inputs as variables to avoid typos
espresso = 'espresso'
latte = 'latte'
cappuccino = 'cappuccino'
off = 'off'
report = 'report'
cents = 0


def user_input():
    prompt = input('What would you like? ').lower()
    if prompt == 'espresso':
        check_resources('espresso')
    if prompt == 'latte':
        check_resources('latte')
    if prompt == 'cappuccino':
        check_resources('cappuccino') 
    if prompt == 'report':
        print_report()


def check_resources(drink_name):
    drink_ingredients = data.MENU[drink_name]['ingredients']
    for ingred in drink_ingredients:
        #print(ingred)
        #print(drink_ingredients[ingred])
        #print(data.resources[ingred])
        if drink_ingredients[ingred] > data.resources[ingred]:
            print('out')
            break
    else:
        print('Please insert coins uwu')
        take_money()
            

def take_money():
    monies = []
    quarters = int(input('Quarters: '))*25
    dimes = int(input('Dimes: '))*10
    nickels = int(input('Nickels: '))*5
    pennies = int(input('Pennies: '))
    monies.append(quarters)
    monies.append(dimes)
    monies.append(nickels)
    monies.append(pennies)
    return sum(monies)

def print_report():
    values = data.resources
    for key in values:
        print(f'{key} : {values[key]} ')
    

#print_report()
user_input()
