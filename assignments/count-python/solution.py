def main():
    # NOTE: This passage was taken from the Python Reader (https://codeinplace.stanford.edu/cip5/textbook)
    filename = "FileReadingPassage.txt"

    # Initialize a counter for the word
    count = 0

    word = input("Enter a word to count: ")

    # Open the file for reading ('r')
    with open(filename, 'r') as file:
        # Loop over each line and count the occurrences of the word
        for line in file:
            # Convert to lowercase to make the search case-insensitive
            line = line.lower()

            # Count occurrences of word in the line
            count += line.count(word)

    # Print the total count
    print(f"The word '{word}' appears {count} times in the file.")

if __name__ == "__main__":
    main()
