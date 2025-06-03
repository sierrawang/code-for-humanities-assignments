import random

def main():
    # Initialize a random number
    num = random.randint(1, 100)
    
    # Loop until we find a random number that is greater than or equal to 50
    while not (num >= 50 and num % 7 == 0):
        # Print message to user
        print(f"{num} is not lucky enough...")

        # Get a new random number
        num = random.randint(1, 100)

    print(f"Found you a lucky number! {num}")

if __name__ == '__main__':
    main()