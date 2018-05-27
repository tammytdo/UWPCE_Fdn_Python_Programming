"""

Module 3 - Lab 2

UNFINISHED

"""

import random

# Number guess
# Create a script that asks a user to guess a number

# Pick the number randomly from between 1 and 10
random_number = random.randint(1, 10)
print(random_number)
# Give the user 3 attempts to guess the number.
tries = 3
user_guess = int(input("guess a number between 1 and 10: "))
tries -= 1

while tries > 0:
    # give hints on if they need to guess lower or higher.
    if user_guess == random_number:
        print("You guessed my number!")
        break
    elif user_guess > random_number:
        user_guess = int(input("guess a lower number: "))
        tries -= 1
    elif user_guess < random_number:
        user_guess = int(input("guess a higher number: "))
        tries -= 1
print("Game over")
