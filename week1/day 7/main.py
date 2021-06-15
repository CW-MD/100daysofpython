#HangMan
import random

word_list=['cat', 'monkey', 'pneumonoultramicroscopicsilicovolcanoconiosis']

chosen_word = random.choice(word_list)

print(f'word is {chosen_word}')

display = []

for letter in chosen_word:
     display.append('_')
print(display)

previous_guesses = []

lives = 6

win = False

while win != True:
    guess = input('please guess a letter').lower()
    if guess not in previous_guesses:
        previous_guesses.append(guess)
        if guess in chosen_word:
            for x in range(len(display)):
                if chosen_word[x] ==guess :
                    display[x] = guess
                    print(display)
                    if '_' not in display:
                        win=True
        else:
            lives-=1
            print(f'word does not contain {guess}; {lives} lives remain')
            if lives < 1:
                print('You Lose')
                break
    else:
        print(f'{guess} was already guessed')
if win == True:
    print(f'You Win! The word was: {chosen_word}')
    