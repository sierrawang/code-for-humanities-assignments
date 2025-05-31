OZ_PER_COIN = 0.27
DOLLAR_PER_OZ = 3308.60  # as of May 31, 2025

def main():
    # Get number of gold coins from the user
    coins = int(input("Enter number of gold doubloons in the pirate chest: "))

    # Calculate value
    value = coins * OZ_PER_COIN * DOLLAR_PER_OZ

    # Print result
    print(f"Your {coins} gold doubloons are worth ${value} today!")

if __name__ == '__main__':
    main()
