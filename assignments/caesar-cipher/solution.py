
alphabet = 'abcdefghijklmnopqrstuvwxyz'
most_common_letters = 'etaoinshrdlu'

def encrypt(message, shift):
    # Initialize an empty string to hold the encrypted message
    encrypted_message = ''

    # Loop through each letter in the message
    for letter in message:
        # Determine the index of the letter in the alphabet
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                # Calculate the new index with the shift
                new_index = (i + shift) % len(alphabet)
                # Append the corresponding letter from the alphabet to the encrypted message
                encrypted_message += alphabet[new_index]
                break
            elif i == len(alphabet) - 1:
                # If the letter is not in the alphabet, just append it as is
                encrypted_message += letter

    return encrypted_message

# Decrypt the given message based on the likelihood of the letters
def decrypt(message):

if __name__ == '__main__':
    message = input('Enter the message to encrypt: ')
    shift = int(input('Enter the shift value: '))
    encrypted_message = encrypt(message, shift)
    print(f'Encrypted message: {encrypted_message}')