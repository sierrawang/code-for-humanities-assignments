import random

def play_game():
    # Define the choices
    choices = ["rock", "paper", "scissors"]

    # Get the user's choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Validate the user's choice
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
    else:
        # Randomly select the computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif ((user_choice == "rock" and computer_choice == "scissors") or 
              (user_choice == "paper" and computer_choice == "rock") or 
              (user_choice == "scissors" and computer_choice == "paper")):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play_game()