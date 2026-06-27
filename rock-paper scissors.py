# Rock-Paper-Scissors Game
import random
# Score variables
user_score = 0
computer_score = 0
print("=== Rock Paper Scissors Game ===")
print("Instructions:")
print("Type rock, paper, or scissors to play.\n")
while True:
    # User input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    # Check valid input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break

    print()