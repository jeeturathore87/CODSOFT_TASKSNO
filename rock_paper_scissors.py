import random

CHOICES = ["rock", "paper", "scissors"]


def get_winner(user, computer):
    if user == computer:
        return "tie"

    if (
        (user == "rock" and computer == "scissors")
        or (user == "scissors" and computer == "paper")
        or (user == "paper" and computer == "rock")
    ):
        return "user"

    return "computer"


def main():
    user_score = 0
    computer_score = 0

    print("\n===== ROCK-PAPER-SCISSORS =====")

    while True:
        user = input("\nChoose rock, paper, scissors (or q to quit): ").lower().strip()

        if user == "q":
            break

        if user not in CHOICES:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(CHOICES)
        print("Computer chose:", computer)

        winner = get_winner(user, computer)

        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win!")
            user_score += 1
        else:
            print("Result: Computer wins!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Play again? (y/n): ").lower().strip()
        if play_again != "y":
            break

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
