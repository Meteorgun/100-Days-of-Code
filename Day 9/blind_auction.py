from art import logo
import os
auction = {}
print(logo)

while True:
    name = input("What is your name? ")
    offer = input("What is your offer? ")
    auction[name] = offer
    other = input("Any other offers? Press Y or N: ")
    if other == "Y":
        os.system("cls")
    elif other == "N":
        break
winner = max(auction.values())
print(f"The winner with the offer of {winner}, wins!")
