# Demo:
# https://appbrewery.github.io/python-day12-demo/

import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
numbers_list = range(1, 101)
answer = random.choice(numbers_list)


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempt = 10
    print(f"You have {attempt} attempts remaining to guess the number.")
elif difficulty == 'hard':
    attempt = 5
    print(f"You have {attempt} attempts remaining to guess the number.")
else:
    print("Invalid difficulty selected, defaulting to 'easy'.")
    attempt = 10


game_over = False
while not game_over and attempt > 0:
    guess = int(input("Make a guess: "))

    if guess > answer:
        attempt -= 1
        print("Too High.")
    elif guess < answer:
        attempt -= 1
        print("Too Low.")
    else:
        print(f"You got it! The answer was {answer}.")
        game_over = True
        break

    if attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
    else:
        print("You are out of attempts. Game over.")
        print(f"The correct number was {answer}.")
        game_over = True
