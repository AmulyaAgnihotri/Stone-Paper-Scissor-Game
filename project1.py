# Stone–Paper–Scissor game
import random

# List of choices
choices = ["stone", "paper", "scissor"]

# Computer choice
computer = random.choice(choices)

# User input
user = input("Enter stone, paper, or scissor: ").lower()

print("Computer chose:", computer)

# Game logic
if user == computer:
    print("It's a tie!")

elif user == "stone":
    if computer == "scissor":
        print("You win!")
    else:
        print("Computer wins!")

elif user == "paper":
    if computer == "stone":
        print("You win!")
    else:
        print("Computer wins!")

elif user == "scissor":
    if computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")

else:
    print("Invalid input. Please choose stone, paper, or scissor.")