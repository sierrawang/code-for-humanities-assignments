import random

def print_dice_histogram():
    num_rolls = int(input("Enter the number of rolls: "))

    counts = {}

    # Simulate rolling the dice
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        if roll in counts:
            counts[roll] += 1
        else:
            counts[roll] = 1

    # Print the histogram
    for i in range(1, 7):
        count = counts.get(i, 0)
        print(f"{i}: {'*' * count} ({count})")

if __name__ == "__main__":
    print_dice_histogram()