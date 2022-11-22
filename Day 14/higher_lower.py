from data import data
from art import logo
from art import vs
import random

score = 0
print(logo)
while True:
    person_a = dict(random.choice(data).items())
    person_b = dict(random.choice(data).items())
    if person_a == person_b:
        person_b = dict(random.choice(data).items())
    print(
        f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']} {vs}")
    print(
        f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}\n")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
        if person_a["follower_count"] > person_b["follower_count"]:
            score += 1
            print(f"Correct! Your score is {score}\n")
        else:
            print(
                f"The answer was: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
            print(f"You lost! Your score was {score}")
            exit()
    elif answer == "b":
        if person_b["follower_count"] > person_a["follower_count"]:
            score += 1
            print(f"Correct! Your score is {score}\n")
        else:
            print(
                f"The answer was: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
            print(f"You lost! Your score was {score}")
            exit()
