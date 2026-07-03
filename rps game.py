import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")

    else:
        print("Computer Wins!")

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Game Over!")
        break
