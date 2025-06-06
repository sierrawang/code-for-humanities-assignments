from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")

    # Get a secret word
    secret_word = get_random_word()

    for attempt in range(NUM_ATTEMPTS):
        guess = input("Enter your guess: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        # Step 1: Build list of remaining unmatched letters
        remaining_letters = []
        for letter in secret_word:
            remaining_letters.append(letter)

        # Step 2: Initialize correctness list with all "B"
        correctness = ["B", "B", "B", "B", "B"]

        # Step 3: First pass – check for exact matches (G)
        for i in range(5):
            if guess[i] == secret_word[i]:
                correctness[i] = "G"
                remaining_letters[i] = None  # Remove matched letter

        # Step 4: Second pass – check for misplaced letters (Y)
        for i in range(5):
            if correctness[i] == "B":
                for j in range(5):
                    if guess[i] == remaining_letters[j]:
                        correctness[i] = "Y"
                        remaining_letters[j] = None
                        break

        # Step 5: Build formatted output
        result = ""
        for i in range(5):
            if correctness[i] == "G":
                result += f"[{guess[i]}] "
            elif correctness[i] == "Y":
                result += f"({guess[i]}) "
            else:
                result += f"{guess[i]} "

        print("Result:", result.strip())

        if guess == secret_word:
            print(f"Congratulations! You guessed the word in {attempt + 1} tries!")
            return

    print(f"Better luck next time! The correct word was '{secret_word}'.")

if __name__ == "__main__":
    main()
