#Guessing Game
import random
game_over = False
SECRET = random.randint(1,100)
#
modes = {"easy":10,"hard":5}
print(SECRET)

print('Welcome to the Guessing Game')
MODE_CHOICE = input("'easy' or 'hard'? :").lower()

remaining_guesses = modes[MODE_CHOICE]
print('Guess the right number between 1-100 to win')

def guess():
    global SECRET
    global remaining_guesses
    global game_over
    while remaining_guesses > 0 or game_over == False:
        user_guess = int(input('Pick a number: '))

        if user_guess > SECRET:
            remaining_guesses -=1
            print(f'too high, {remaining_guesses} guesses remain')
          
        elif user_guess < SECRET:
            remaining_guesses-=1
            print(f'too low, {remaining_guesses} guesses remain')
        else:
            print('Correct!')
            remaining_guesses -= remaining_guesses
            game_over = True
    else:
        print('Game Over!')


guess()