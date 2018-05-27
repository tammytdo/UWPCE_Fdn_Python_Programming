"""
Module 3 - Lab 3

Guess that Animal! 
Make a word guess game of your favorite animals.   

IN PROGRESS

"""

import random

# Goal: A user must guess an animal name by guessing the letters in the name, one letter at a time. 

# Create a list of animals
animals = ["giraffe", "donkey", "cat", "lion"]

# Pick one animal for each game
rand_animal = random.choice(animals)
print(rand_animal)
# A user gets a number of guesses equal to 3 plus the length of the animal name
unique_letters = set(rand_animal)
guesses = len(unique_letters) + 3
print("Your total number of guesses are", guesses,".")


guessed_letters = set()
correct_letters = set()
overlap = set()
counter = 0 


# Use a while loop to get user input (guess a letter!) until they run out of guesses
while counter < guesses:
    print("Guesses used: ", counter)
    user_guess = input("Guess a letter in my animal name: ")
    print()
    guessed_letters.add(user_guess)
    counter += 1

    # if user guesses a correct letter
    if user_guess in unique_letters:
        print("You guessed a correct letter!")
        correct_letters.add(user_guess)
        if user_guess in correct_letters:
        elif correct_letters.issubset(guessed_letters):
            print("You win!")
            break
        else:
            print("What is your next guess? \n")
        print("Correct letters guesses: ", correct_letters)
        print("All guessed letters: ", guessed_letters, "\n")
    # incorrect letter
    elif correct_letters.issubset(guessed_letters):
        print("You win!")
        break
    else:
        print("Incorrect letter. Guess again. \n")
    # if correct_letters.issubset(guessed_letters):
    #     print("You win!")
    #     break

print("End of game")