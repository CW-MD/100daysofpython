#HangMan
import random

word_list=['cat', 'monkey', 'pneumonoultramicroscopicsilicovolcanoconiosis']

chosen_word = random.choice(word_list)

guess = input('please guess a letter').lower()

previous_guesses = []

lives = 6

if guess not in previous_guesses:
    previous_guesses.append(guess)
    if guess in chosen_word:
        for letter in chosen_word:
            if letter == guess:
                print(guess)
            else:
                print('?')
    else:
        lives-=1
        print(f'word does not contain {guess}; {lives} lives remain')
else:
    print(f'{guess} was already guessed')