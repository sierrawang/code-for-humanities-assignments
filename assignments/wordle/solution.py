from words import get_random_word

# The user has 6 attempts
NUM_ATTEMPTS = 6

# Return a list with:
# - a G for each letter that is the correct value and position
# - a Y for each letter that is the correct value and wrong position
# - a B otherwise
def evaluate_correctness(true_word, guess_word):
    # Initialize a list of letters that need to be found
    remaining_letters = []
    for letter in true_word:
        remaining_letters.append(letter)

    # Initialize the correctness list
    correctness = ["B", "B", "B", "B", "B"]

    # Determine positions with correct value and position
    for i in range(5):
        # Check if the letter matches exactly.
        if guess_word[i] == true_word[i]:
            # Update the correctness list
            correctness[i] = "G"

            # Update the remaining letters list
            remaining_letters[i] = None

    # Determine letters that are not in the correct position
    for i in range(5):
        # Check if letter has not already been guessed and is in the remaining letters
        if correctness[i] == "B":
            # Determine if the guessed letter is in the remaining letters:
            for j in range(5):
                if guess_word[i] == remaining_letters[j]:
                    correctness[i] = "Y"
                    remaining_letters[j] = None

    return correctness

# Return the guess word formatted where
# each correct letter is in brackets []
# and each incorectly placed letter is in ()
# and all other letters are as is
def get_formatted_guess(correctness, guess_word):
    # Initialize a result string
    result_str = ""

    # Loop over the guess word and 
    for i in range(5):
        if correctness[i] == "G":
            result_str += f"[{guess_word[i]}] "
        elif correctness[i] == "Y":
            result_str += f"({guess_word[i]}) "
        else:
            result_str += f"{guess_word[i]} "

    return result_str

def main():
    print("Welcome to wordle!")

    # Get a random word
    true_word = get_random_word()

    for attempt in range(1, NUM_ATTEMPTS + 1):
        guess_word = input(f"Enter your next guess: ").lower()

        if guess_word == true_word:
            print(f"Congratulations! You guessed the word '{true_word}' in {attempt} tries!")
            return

        # Get a list indicating the correctness of the guess
        correctness = evaluate_correctness(true_word, guess_word)

        # Get the formatted guess
        formatted_guess = get_formatted_guess(correctness, guess_word)

        print(f"Result: {formatted_guess}")
        print()

        if attempt == NUM_ATTEMPTS:
            print(f"Better luck next time! The correct word was {true_word}.")

if __name__ == "__main__":
    main()