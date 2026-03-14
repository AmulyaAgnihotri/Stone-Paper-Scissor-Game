from enum import Enum
import random

# Define choices using Enum (modern Python style)
class Choice(Enum):
    STONE = "stone"
    PAPER = "paper"
    SCISSOR = "scissor"

# Function to get computer choice
def get_computer_choice():
    return random.choice(list(Choice))

# Function to decide winner
def decide_winner(user, computer):
    match (user, computer):
        case (Choice.STONE, Choice.SCISSOR) | (Choice.PAPER, Choice.STONE) | (Choice.SCISSOR, Choice.PAPER):
            return "user"
        case (Choice.SCISSOR, Choice.STONE) | (Choice.STONE, Choice.PAPER) | (Choice.PAPER, Choice.SCISSOR):
            return "computer"
        case _:
            return "tie"

# Game loop
def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Stone-Paper-Scissor Game")

    while True:
        user_input = input("\nEnter stone, paper, scissor or quit: ").lower()

        if user_input == "quit":
            break

        try:
            user_choice = Choice(user_input)
        except ValueError:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice.value}")
        print(f"Computer chose: {computer_choice.value}")

        winner = decide_winner(user_choice, computer_choice)

        if winner == "user":
            print("✅ You win!")
            user_score += 1
        elif winner == "computer":
            print("💻 Computer wins!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

        print(f"Score → You: {user_score} | Computer: {computer_score}")

    print("\nThanks for playing!")

# Run game
if __name__ == "__main__":
    play_game()
