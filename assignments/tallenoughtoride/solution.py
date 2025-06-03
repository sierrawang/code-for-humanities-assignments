MINIMUM_HEIGHT = 50  # Arbitrary units :)

def main():
    # Ask the user for a height to check
    height = input("How tall are you? ")

    # If the user presses Enter immediately (without typing anything),
    # the result of input() will be an empty string (nothing between the quotation marks!)
    while height != "":
        height = float(height)  # Convert non-empty strings to be a float!
        
        # Perform height check
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

        # Ask the user for another height to check
        height = input("How tall are you? ")

if __name__ == '__main__':
    main()