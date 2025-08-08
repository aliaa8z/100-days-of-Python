# Demo:
# https://appbrewery.github.io/python-day4-demo/

import random 

visual = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', 
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', 
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
''']


def game(user, computer):
    if user == computer:
        print("It's a draw")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print('You win!')
    else:
        print('You lose')


options = [0, 1, 2]
computer = random.choice(options)

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

print(visual[user])
print(f"\nComputer chose: \n{visual[computer]}\n")

game(user= user, computer= computer)