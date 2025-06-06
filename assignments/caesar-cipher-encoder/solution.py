ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def main():
    # Get a message and a shift from the user
    message_to_encrypt = input("Enter a message: ")
    shift = int(input("Enter a shift number: "))
    
    # Initialize the encrypted message
    encrypted_message = ""

    # Loop over every character in the message
    # and add the shifted character
    for letter in message_to_encrypt:
        if letter.isalpha():
            # Store a boolean for whether the letter is uppercase
            is_uppercase = letter.isupper()

            # Make sure the letter is lowercase
            letter = letter.lower()

            # Get the index of the current character in the alphabet
            index = ALPHABET.index(letter)
            
            # Get the shifted index
            shifted_index = (index + shift) % len(ALPHABET)

            # Get the letter to add
            new_letter = ALPHABET[shifted_index]

            # Convert it to uppercase if the original letter was uppercase
            if is_uppercase:
                new_letter = new_letter.upper()

            # Append the new letter to the encrypted message
            encrypted_message += new_letter
        else:
            # The letter is not in the alphabet (e.g., _, 3, ...)
            # Just append the character unencrypted
            encrypted_message += letter

    print("Encrypted message:", encrypted_message)

if __name__ == '__main__':
    main()