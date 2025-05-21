
def play_game():
    # Start with 20 stones
    current_stones = 20
    current_player = 1

    while current_stones > 0:
        print(f"There are {current_stones} stones left.")
        
        # Get the next amount to remove
        num_remove = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))
        while num_remove != 1 and num_remove != 2:
            num_remove = int(input("Please enter 1 or 2: "))
        print()

        # Update the current stones count
        current_stones -= num_remove
        
        # Update the current_player
        current_player = current_player % 2 + 1

    print(f"Player {current_player} wins!")

if __name__ == '__main__':
    play_game()