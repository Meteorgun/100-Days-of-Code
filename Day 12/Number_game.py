#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
easy_lives = 10
hard_lives = 5
number = random.randint(0, 100)
print(logo)
print("Welcom to the number guessing game!")
print("I'm thinking of a number between 1 and 100")


game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_mode == "easy":
    while True:
        if easy_lives == 0:
            print(f"You lost! The number was {number}")
            exit()
        print(f"You have {easy_lives} attempts remaining to guess the number")
        easy_guess = int(input("Make a guess: "))
        if easy_guess == number:
            print(f"You have guessed the number! {number}")
            print(f"You had {easy_lives} attempts left")
            exit()
        elif easy_guess > number:
            easy_lives -= 1
            print("Too high\nGuess again")
        else:
            easy_lives -= 1
            print("Too low\nGuess again")
elif game_mode == "hard":
    while True:
        if hard_lives == 0:
            print(f"You lost! The number was {number}")
            exit()
        print(f"You have {hard_lives} attempts remaining to guess the number")
        hard_guess = int(input("Make a guess: "))
        if hard_guess == number:
            print(f"You have guessed the number! {number}")
            print(f"You had {hard_lives} attempts left")
            exit()
        elif hard_guess > number:
            hard_lives -= 1
            print("Too high\nGuess again")
        else:
            hard_lives -= 1
            print("Too low\nGuess again")
