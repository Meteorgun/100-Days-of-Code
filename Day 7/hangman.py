import random
from turtle import position
from hangman_art import logo, stages
from hangman_words import word_list

display = []
word = random.choice(word_list)
lives = 6
guessed_letter = []

for i in word:
    display.append("_")

print(word)
while "_" in display and lives > 0:
    print(f"You have {lives} lives left")
    print(f"You have already guess {guessed_letter}")
    guess = input("Guess your letter: ")
    guessed_letter += guess
    for position in range(len(word)):
        letter = word[position]
        if guess == letter:
            display[position] = guess
    if "_" not in display:
        print("You have won the game \nCongratulations!")
    if guess not in word:
        lives -= 1
    if lives == 0:
        print(f"The word is {word}")
        print(f"You have lost! Game Over!")
    print(stages[lives])
    print(display)
