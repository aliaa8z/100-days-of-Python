# Demo
# https://appbrewery.github.io/python-day7-demo/

import random

lives = 6

words = ['apple', 'banana', 'orange', 'strawberry']
word = random.choice(words)
print(word)

placewholder = ""
for _ in range(len(word)):
    placewholder += "_"
print(placewholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input('Guess a letter: ').lower()

    display = ""

    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You Lose')

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(f"you have {lives} left")