# Demo:
# https://appbrewery.github.io/python-day5-demo/

import string
import random

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

letters = list(string.ascii_letters)
symbols = ['-', '*', '?', '+', '<', '>', ')', "("]
numbers = [str(i) for i in range(0,10)]

res = []
for _ in range(num_letters):
    ch = random.choice(letters)
    res.append(ch)

for _ in range(num_symbols):
    ch = random.choice(symbols)
    res.append(ch)

for _ in range(num_numbers):
    ch = random.choice(numbers)
    res.append(ch)

print(res)
random.shuffle(res)
print(res)
print(f"Your password is: {''.join(res)}")
