#Rock Paper Scissors
#Rock == 0, Paper == 1, Scissors == 2
import ascii, random

choices = {0:'Rock', 1:'Paper', 2:'Scissors'}
print('Rock Paper Scissors')
userPick = int(input('Please Pick a number between 0 - 2 for your choice \nRock: 0\nPaper: 1\nScissors: 2  \n'))
computerPick = random.randint(0,2)
print(f'User: {userPick} -- Computer: {computerPick}')
print(choices[userPick])
if userPick == computerPick:
    print(f'Draw! You both picked {choices[userPick]}')
    
#Rock Logic
if userPick == 0 and computerPick != userPick:
    print(f"You Picked: \n{ascii.rock}")
    if computerPick == 1:
        print(f"Computer Picked: \n {ascii.paper}")
        print('You Lose!')
    else:
        print(f"Computer Picked: \n{ascii.scissors}")
        print('You Win!')

#Paper Logic
if userPick == 1 and computerPick != userPick:
    print(f"You Picked: \n{ascii.paper}")
    if computerPick == 2:
        print(f"Computer Picked: \n {ascii.scissors}")
        print('You Lose!')
    else:
        print(f"Computer Picked: \n{ascii.rock}")
        print('You Win!')

#Scissors Logic
if userPick == 2 and computerPick != userPick:
    print(f"You Picked: \n{ascii.scissors}")
    if computerPick == 0:
        print(f"Computer Picked: \n {ascii.rock}")
        print('You Lose!')
    else:
        print(f"Computer Picked: \n{ascii.paper}")
        print('You Win!')




