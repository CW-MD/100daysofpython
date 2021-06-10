print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


input1 = input('left or right?').lower()
if input1 == 'left':
    print('You died!')
else:
    input2 = input('You come across a 3-way split. Do you want to go left, straight, or right?').lower()
    if input2 == 'left':
        print('You died!')
    elif input2 == 'straight':
        print('Ded')
    else:
        input3 = input('You see a large building with three doors: red, yellow, and blue. Which color will you choose? ').lower()
        if input3 == 'red':
            print('Upon opening the door you are immediately engulfed in flames. #ded')
        elif input3 == 'blue':
            print("You walk through the door and find yourself sinking. This isn't a home, it's an abyss. #ded")
        else:
            print("Winner Winner Chicken Dinner (please don't sue me). Upon entering the home you are greeted by a treasure chest. If only you had the dlc to unlock it... #Winner")
