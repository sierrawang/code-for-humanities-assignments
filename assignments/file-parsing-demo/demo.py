import json

# Remove any non letters and make the word lowercase
def get_clean_word(word):
    # Initialize a clean word string
    clean_word = ""

    # Add each letter of the word
    for ch in word:
        if ch.isalpha():
            clean_word += ch

    # Make it lowercase
    clean_word = clean_word.lower()

    return clean_word

# Write the word counts to an output file
def output_word_counts(word_counts, output_filename):
    # Open the file for writing
    with open(output_filename, 'w') as file:
        # Loop over my dictionary and output each key-value pair on a new line
        for word in word_counts:
            file.write(f"{word}: {word_counts[word]}\n")

# Return a dictionary of the word counts in the file
def get_word_counts(input_filename):

    # Initialize my word_counts dictionary
    word_counts = {}

    # Open the file
    with open(input_filename, 'r') as file:
        # Buggy version: for line in file.readline():
        
        # Get the lines of the file
        lines = file.readlines()
        # print(lines)

        # Loop over the lines
        for bob in lines:
            
            # Loop over each word in this line and add it to my counts dictionary
            words = bob.split()
            
            for word in words:
                # Clean my word by making it lowercase and removing punctuation
                word = get_clean_word(word)

                # Update my word_counts dictionary
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts

# Write the dictionary to the json output file
def output_word_counts_as_json(word_counts, output_filename):
    with open(output_filename, 'w') as bob:
        json.dump(word_counts, bob)

def main():
    # 
    input_filename = "./sample_input.txt" # ./ means in the same directory
    word_counts = get_word_counts(input_filename)

    output_filename = "./another_output.txt"
    output_word_counts(word_counts, output_filename)
    
    output_filename_json = "./json_output.json"
    output_word_counts_as_json(word_counts, output_filename_json)

if __name__ == '__main__':
    main()