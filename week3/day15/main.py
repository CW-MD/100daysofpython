#Coffee Machine
import data
#
machine_money = 0


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
    global machine_money
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
        money_input = take_money()
        if money_input >= data.MENU[drink_name]['cost']:
            machine_money += issue_change(money_input, drink_name)
            deduct_resources(drink_name)
            print(f'Here is your {drink_name}')
        else:
            print('need more money')
            

def take_money():
    monies = []
    quarters =int(input('Quarters: '))*25
    dimes = int(input('Dimes: '))*10
    nickels = int(input('Nickels: '))*5
    pennies = int(input('Pennies: '))
    monies.append(quarters)
    monies.append(dimes)
    monies.append(nickels)
    monies.append(pennies)
    return (sum(monies) / 100)

def print_report():
    values = data.resources
    for key in values:
        print(f'{key} : {values[key]} ')
    

def issue_change(money, drink_name):
    cost = float(data.MENU[drink_name]['cost'])
    change = (money - cost)
    print(f'Your change is ${round(change,5)}')
    return cost
    
def deduct_resources(drink_name):
    drink_ingredients = data.MENU[drink_name]['ingredients']
    for ingred in drink_ingredients:
        data.resources[ingred] -= drink_ingredients[ingred]
        
        
user_input()
