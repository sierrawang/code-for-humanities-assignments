# Remove any non letters and make the word lowercase
def get_clean_word(word):
    # Init a clean word string
    clean_word = ""

    # Add each letter of the word to the result
    for ch in word:
        if ch.isalpha():
            clean_word += ch

    # Make the clean word lowercase
    clean_word = clean_word.lower()

    return clean_word

# Write the word counts to an output file
def output_word_counts(word_counts, output_filename):
    with open(output_filename, 'w') as file:
        for word in word_counts:
            file.write(f"{word}: {word_counts[word]}\n")

# Return a dictionary of the word counts in the file
def get_word_counts(input_filename):
    # Initialize empty counts dictionary
    word_counts = {}

    with open(input_filename, 'r') as file:
        for line in file:
            # Remove leading and trailing spaces
            line = line.strip()

            # Split the line by spaces
            words = line.split()

            # Add each word to the dictionary
            for word in words:
                # Remove punctuation from word and make it lowercase
                word = get_clean_word(word)

                # Update counts
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    
    return word_counts

def main():
    input_filename = "./sample_input.txt"
    word_counts = get_word_counts(input_filename)

    output_filename = "./sample_output.txt"
    output_word_counts(word_counts, output_filename)
    
if __name__ == '__main__':
    main()